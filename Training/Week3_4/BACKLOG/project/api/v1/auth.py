
from sqlmodel import select
from core.security import create_refresh_token,verify_password,create_access_token,verify_token
from fastapi import HTTPException
from models.models import User
from fastapi import Depends
from schemas.auth import LoginRequest
from schemas.auth import LoginResponse
from fastapi import APIRouter,Response
from db.db_config import get_session
from sqlmodel import Session

public_auth_router = APIRouter(prefix="/auth")
private_auth_router = APIRouter(prefix="/auth",dependencies=[Depends(verify_token)])


@public_auth_router.post("/login",response_model=LoginResponse)
def login(login_request:LoginRequest,
response:Response,
session:Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.email == login_request.email)).first()
    if user is None:
        raise HTTPException(status_code=403,detail="user not found")

    if not verify_password(login_request.password,user.password):
        raise HTTPException(status_code=403,detail="password not match")

    access_token = create_access_token(user.id,user.role)
    refresh_token = create_refresh_token(user.id,user.role)

    response.set_cookie("refresh_token",
    refresh_token,
    httponly=True,
    secure=True,
    samesite="strict",
    max_age=60*60*24*7
    )

    return LoginResponse(
        access_token=access_token
    )


@private_auth_router.post("/logout")
def logout(response:Response):
    response.delete_cookie("refresh_token")
    return {"message":"Logout successfully"}
