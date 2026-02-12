from core.security import create_access_token, create_refresh_token
from core.hash import verify_password
from fastapi import HTTPException
from http import HTTPStatus
from repository.user_repository import UserRepository
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import UserRead
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Response
from db.db_config import get_session
from service.redis_service import RedisService
from core.security import parse_token
from fastapi.security import HTTPAuthorizationCredentials
from datetime import datetime

class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def login(self, login_request: OAuth2PasswordRequestForm):
        user = await self.repository.get_by_email(login_request.username)

        if user is None:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, 
                detail="User not found"
            )

        if not verify_password(login_request.password, user.password):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, 
                detail="Password does not match"
            )

        access_token = create_access_token(user.id, user.role)
        refresh_token = create_refresh_token(user.id, user.role)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": UserRead.model_validate(user)
        }

    async def logout(
        self, 
        response: Response, 
        redis_service: RedisService, 
        credentials: HTTPAuthorizationCredentials
    ):
        try:
            payload = await parse_token(credentials, redis_service)
            if payload:
                ttl = payload.exp - int(datetime.now().timestamp())
                await redis_service.add_to_cache(credentials.credentials, payload.sub, ttl=max(0, ttl))
            
            response.delete_cookie("refresh_token")
            return {"message": "Logout successfully"}
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"Error occurred during logout: {str(e)}"
            )

def get_auth_service(session: AsyncSession = Depends(get_session)):
    return AuthService(UserRepository(session))
