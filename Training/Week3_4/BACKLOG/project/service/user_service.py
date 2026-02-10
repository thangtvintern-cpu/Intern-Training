from schemas.user import UserRead
from sqlalchemy.ext.asyncio import AsyncSession
from service.redis_service import get_redis_service
from service.redis_service import RedisService
from core.decorators import cache_checker, cache_validator
from schemas.user import UserUpdate
from schemas.user import UserCreate
from http import HTTPStatus
from fastapi import HTTPException
from db.db_config import get_session
from fastapi import Depends
from service.base_service import BaseService
from repository.user_repository import UserRepository
from models.models import User
from bcrypt import hashpw, checkpw, gensalt


class UserService(BaseService[User]):
    def __init__(self, repository: UserRepository, cache_service: RedisService):
        super().__init__(repository, cache_service)

    @staticmethod
    def get_password_hash(password: str):
        return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    async def get_user_by_email(self, email: str):
        user = await self.repository.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="User not found"
            )
        return UserRead.model_validate(user)

    async def exists_user_by_email(self, email: str):
        return await self.repository.exists_by_email(email)

    @cache_checker(lambda offset,limit: f"users:{offset}:{limit}", ttl=60 * 5)
    async def get_user_with_pagination(self, offset: int, limit: int):
        users = await self.repository.get_by_pagination(offset, limit)
        return [UserRead.model_validate(user) for user in users]

    @cache_checker(lambda id: f"user:{id}", ttl=60 * 5)
    async def get_user_by_id(self, id: int):
        user_model = await self.repository.get_by_id(id)
        if not user_model:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="User not found"
            )
        return UserRead.model_validate(user_model)
    
    @cache_validator(pattern="user:*")
    async def create_user(self, user: UserCreate):
        if await self.exists_user_by_email(user.email):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail="User already exists"
            )
        user_model = User(**user.model_dump())
        user_model.password = self.get_password_hash(user.password)
        return UserRead.model_validate(await self.repository.create(user_model))
    
    @cache_validator(pattern="user:*")
    async def delete_user(self, id: int):
        user_model = await self.get_user_by_id(id)
        if not user_model:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="User not found"
            )
        return await self.repository.delete(user_model)
    
    @cache_validator(pattern="user:*")
    async def update_user(self, user: UserUpdate, current_user: User):
        user_data = user.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(current_user, key, value)
        return UserRead.model_validate(await self.repository.update(current_user))


def get_user_service(
    session: AsyncSession = Depends(get_session), cache_service: RedisService = Depends(get_redis_service)
):
    return UserService(UserRepository(session), cache_service)

