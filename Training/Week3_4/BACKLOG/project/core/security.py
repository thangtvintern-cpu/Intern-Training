from service.redis_service import RedisService, get_redis_service
from uuid import UUID
from models.models import User
from db.db_config import get_session
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import Depends
from core.config import AppSettings
from datetime import timedelta
from datetime import datetime
from pydantic import BaseModel
from jose import JWTError, jwt
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from schemas.user import UserRole
from typing import Annotated
settings = AppSettings()
SECRET_KEY = settings.SECRET_KEY

security = HTTPBearer()


class TokenPayLoad(BaseModel):
    sub: str
    exp: int
    type: str
    role: str


def create_access_token(
    sub: UUID, role: UserRole, expires_delta: timedelta = timedelta(days=1)
):
    expires_at = datetime.utcnow() + expires_delta
    payload = {"sub": str(sub), "role": role, "type": "access", "exp": expires_at}

    return jwt.encode(payload, SECRET_KEY, algorithm=settings.jwt_algorithm)


def create_refresh_token(
    sub: UUID, role: UserRole, expires_delta: timedelta = timedelta(days=7)
):
    expires_at = datetime.utcnow() + expires_delta
    payload = {"sub": str(sub), "role": role, "type": "refresh", "exp": expires_at}

    return jwt.encode(payload, SECRET_KEY, algorithm=settings.jwt_algorithm)


async def parse_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    redis_service: RedisService = Depends(get_redis_service),
) -> TokenPayLoad | None:
    token = credentials.credentials
    if not token:
        raise HTTPException(status_code=401, detail="Không có token trong request")

    if await redis_service.exists_in_cache(token):
        raise HTTPException(status_code=401, detail="Token đã bị thu hồi")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[settings.jwt_algorithm])
        return TokenPayLoad(**payload)
    except JWTError:
        return None


async def get_current_user(
    payload: TokenPayLoad = Depends(parse_token),
    session: Session = Depends(get_session),
):
    if payload is None or payload.type != "access":
        raise HTTPException(status_code=401, detail="Token không hợp lệ")

    user = await session.get(User, payload.sub)
    if user is None:
        raise HTTPException(status_code=401, detail="User không tồn tại")
    return user


def require_roles(allowed_roles: list[UserRole]):
    def role_check(current_user: User = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=403, detail="Bạn không có quyền truy cập tài nguyên này"
            )
        return current_user

    return role_check


AdminRoleDep = Annotated[User, Depends(require_roles([UserRole.ADMIN]))]

UserRoleDep = Annotated[User, Depends(require_roles([UserRole.USER, UserRole.ADMIN]))]
