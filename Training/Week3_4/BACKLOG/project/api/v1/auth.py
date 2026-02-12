from core.security import security
from fastapi.security import HTTPAuthorizationCredentials, OAuth2PasswordRequestForm
from service.redis_service import get_redis_service
from service.redis_service import RedisService
from http import HTTPStatus
from core.security import parse_token
from fastapi import Depends
from fastapi import APIRouter, Response
from service.auth_service import get_auth_service, AuthService

public_auth_router = APIRouter(prefix="/auth", tags=["v1 - auth"])
private_auth_router = APIRouter(
    prefix="/auth", dependencies=[Depends(parse_token)], tags=["v1 - auth"]
)


@public_auth_router.post("/login", status_code=HTTPStatus.OK)
async def login(
    response: Response,
    login_request: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service),
):
    login_result = await auth_service.login(login_request)
    
    access_token = login_result["access_token"]
    refresh_token = login_result["refresh_token"]

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
    auth_service: AuthService = Depends(get_auth_service),
    redis_service: RedisService = Depends(get_redis_service),
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    return await auth_service.logout(response, redis_service, credentials)
