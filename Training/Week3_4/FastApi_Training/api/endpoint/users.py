
from DTO.create_user_request import CreateUserRequest
from fastapi import APIRouter
from typing import Annotated
from DTO.login_request import LoginRequest,LoginResponse
from fastapi import Body
from repository.user_repository import get_user_repository

router = APIRouter(prefix='/users', tags=['users'])
user_repo = get_user_repository()


@router.post('/login', response_model=LoginResponse)
def login(user:Annotated[LoginRequest,Body(embed=True)]):
    if user_repo.login(user.model_dump()):
        return {'access_token':user_repo.get_user_by_email(user.email)['access_token'],
        'refresh_token':user_repo.get_user_by_email(user.email)['refresh_token']}
    return {'message':'Login failed'}

@router.post('/create-user')
def create_user(user:Annotated[CreateUserRequest,Body(embed=True)]):
    if user_repo.create_user(user.model_dump()):
        return {'message':'Create user failed'}
    return {'message':'Create user success'}
