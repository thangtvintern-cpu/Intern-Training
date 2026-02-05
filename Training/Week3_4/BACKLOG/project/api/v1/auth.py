from core.security import security
from fastapi.security import HTTPAuthorizationCredentials, OAuth2PasswordRequestForm
from datetime import datetime
from service.redis_service import get_redis_service
from service.redis_service import RedisService
from http import HTTPStatus
from sqlmodel import select
from core.security import (
    create_refresh_token,
    create_access_token,
    parse_token,
)
from core.hash import verify_password
from fastapi import HTTPException
from models.models import User
from fastapi import Depends
from fastapi import APIRouter, Response
from db.db_config import get_session
from sqlmodel import Session

public_auth_router = APIRouter(prefix="/auth", tags=["v1 - auth"])
private_auth_router = APIRouter(
    prefix="/auth", dependencies=[Depends(parse_token)], tags=["v1 - auth"]
)


@public_auth_router.post("/login", status_code=HTTPStatus.OK)
def login(
    response: Response,
    login_request: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.exec(
        select(User).where(User.email == login_request.username)
    ).first()

    if user is None:
        raise HTTPException(status_code=403, detail="user not found")

    if not verify_password(login_request.password, user.password):
        raise HTTPException(status_code=403, detail="password not match")

    access_token = create_access_token(user.id, user.role)
    refresh_token = create_refresh_token(user.id, user.role)

    response.set_cookie(
        "refresh_token",
        refresh_token,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=60 * 60 * 24 * 7,
    )

    return {"access_token": access_token}


# ------------------------------------------------------------------------------------------------------------------


# Private Endpoints
@private_auth_router.post("/logout", status_code=HTTPStatus.OK)
async def logout(
    response: Response,
    redis_service: RedisService = Depends(get_redis_service),
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    try:
        payload = await parse_token(credentials, redis_service)
        ttl = payload.exp - int(datetime.now().timestamp())
        await redis_service.add_to_cache(credentials.credentials, payload.sub, ttl=ttl)
        response.delete_cookie("refresh_token")
        return {"message": "Logout successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"{e}" + "Something went wrong when deleting the cookie",
        )
