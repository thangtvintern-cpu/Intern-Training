from schemas.user import UserUpdate
from schemas.user import UserCreate
from http import HTTPStatus
from fastapi import HTTPException
from db.db_config import get_session
from fastapi import Depends
from service.base_service import BaseService
from repository.user_repository import UserRepository
from models.models import User
from sqlmodel import Session
from uuid import UUID
from bcrypt import hashpw, checkpw, gensalt


class UserService(BaseService[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    @staticmethod
    def get_password_hash(password: str):
        return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    def get_user_by_email(self, email: str):
        return self.repository.get_by_email(email)

    def get_user_with_pagination(self, offset: int, limit: int):
        return self.repository.get_by_pagination(offset, limit)

    def get_user_by_id(self, id: str):
        user_model = self.repository.get_by_id(UUID(id))
        if not user_model:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="User not found"
            )
        return user_model

    def create_user(self, user: UserCreate):
        if self.get_user_by_email(user.email):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail="User already exists"
            )
        user_model = User(**user.model_dump())
        user_model.password = self.get_password_hash(user.password)
        return self.repository.create(user_model)

    def delete_user(self, id: str):
        user_model = self.get_user_by_id(id)
        if not user_model:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="User not found"
            )
        return self.repository.delete(user_model)

    def update_user(self, user: UserUpdate, current_user: User):
        user_data = user.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(current_user, key, value)
        return self.repository.update(current_user)

    def get_all_users(self):
        return self.repository.get_all()


def get_user_service(session: Session = Depends(get_session)):
    return UserService(UserRepository(session))
