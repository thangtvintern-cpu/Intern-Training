from uuid import UUID
from http import HTTPStatus
from fastapi import HTTPException
from sqlmodel import select
from core.security import get_current_user, parse_token, UserRole, AdminRole
from core.hash import get_password_hash
from fastapi import APIRouter
from fastapi import Depends
from db.db_config import get_session
from sqlmodel import Session
from models.models import User
from schemas.user import UserCreate, UserUpdate, UserResponse
from service.user_service import UserService, get_user_service

public_user_router = APIRouter(prefix="/users", tags=["v1 - users"])
private_user_router = APIRouter(
    prefix="/users", dependencies=[Depends(parse_token)], tags=["v1 - users"]
)


# Public Endpoints

@public_user_router.post(
    "/", response_model=UserResponse, status_code=HTTPStatus.CREATED
)
def create_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    return user_service.create_user(user)



# ------------------------------------------------------------------------------------------------------------------


# Private Endpoints

@private_user_router.put("/", response_model=UserResponse, status_code=HTTPStatus.OK)
def update_user(
    user: UserUpdate,
    user_service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user),
):
    return user_service.update_user(user,current_user)
    

@private_user_router.get(
    "/", response_model=list[UserResponse], status_code=HTTPStatus.OK
)
def get_users(admin: AdminRole, user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()
    


@private_user_router.get(
    "/{id}", response_model=UserResponse, status_code=HTTPStatus.OK
)
def get_user(admin: AdminRole, id: str,user_service: UserService = Depends(get_user_service)):
    return user_service.get_user_by_id(id)


@private_user_router.delete(
    "/{id}", response_model=UserResponse, status_code=HTTPStatus.OK
)
def delete_user(admin: AdminRole, id: str,user_service: UserService = Depends(get_user_service)):
    return user_service.delete_user(id)


@private_user_router.get("/me",response_model=UserResponse,status_code=HTTPStatus.OK)
def get_current_user(current_user: User = Depends(get_current_user)):
    return current_user