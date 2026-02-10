from fastapi import Query
from typing import Annotated
from schemas.common import Pagination
from http import HTTPStatus
from core.security import get_current_user, parse_token, AdminRoleDep
from fastapi import APIRouter
from fastapi import Depends
from models.models import User
from schemas.user import UserCreate, UserUpdate, UserRead
from service.user_service import UserService, get_user_service

public_user_router = APIRouter(prefix="/users", tags=["v1 - users"])
private_user_router = APIRouter(
    prefix="/users", dependencies=[Depends(parse_token)], tags=["v1 - users"]
)


# Public Endpoints


@public_user_router.post("/", response_model=UserRead, status_code=HTTPStatus.CREATED)
async def create_user(
    user: UserCreate, user_service: UserService = Depends(get_user_service)
):
    return await user_service.create_user(user)


# ------------------------------------------------------------------------------------------------------------------


# Private Endpoints


@private_user_router.put("/", response_model=UserRead, status_code=HTTPStatus.OK)
async def update_user(
    user: UserUpdate,
    user_service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user),
):
    return await user_service.update_user(user, current_user)


@private_user_router.get("/me", response_model=UserRead, status_code=HTTPStatus.OK)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


@private_user_router.get("/{id}", response_model=UserRead, status_code=HTTPStatus.OK)
async def get_user(
    admin: AdminRoleDep, id: int, user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_user_by_id(id)


@private_user_router.delete("/{id}", response_model=UserRead, status_code=HTTPStatus.OK)
async def delete_user(
    admin: AdminRoleDep, id: int, user_service: UserService = Depends(get_user_service)
):
    return await user_service.delete_user(id)


@private_user_router.get("/", response_model=list[UserRead], status_code=HTTPStatus.OK)
async def get_users_with_pagination(
    admin: AdminRoleDep,
    pagination: Annotated[Pagination, Query()],
    user_service: UserService = Depends(get_user_service),
):
    return await user_service.get_user_with_pagination(
        pagination.offset, pagination.limit
    )
