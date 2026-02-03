from http import HTTPStatus
from fastapi import HTTPException
from core.security import verify_token
from sqlmodel import select
from core.security import get_password_hash
from core.security import get_current_user
from fastapi import APIRouter
from fastapi import Depends
from db.db_config import get_session
from sqlmodel import Session
from models.models import User
from schemas.user import UserCreate,UserUpdate,UserResponse

public_user_router = APIRouter(prefix="/users",tags=["v1 - users"])
private_user_router = APIRouter(prefix="/users",dependencies=[Depends(verify_token)],tags=["v1 - users"])



# Public Endpoints
@public_user_router.post("/",response_model=UserResponse,status_code=HTTPStatus.CREATED)
def create_user(user:UserCreate,
session:Session = Depends(get_session),
):  
    try:
        hashed_pw = get_password_hash(user.password)
        user_model = User.from_orm(user)
        user_model.password = hashed_pw
        session.add(user_model)
        session.commit()
        session.refresh(user_model)
        return user_model
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail=f"{e}" + "Something went wrong")



#------------------------------------------------------------------------------------------------------------------


# Private Endpoints
@private_user_router.put("/",response_model=UserResponse,status_code=HTTPStatus.OK)
def update_user(user:UserUpdate,
session:Session = Depends(get_session),
current_user:User = Depends(get_current_user)
):
    try:
        user_data = user.model_dump(exclude_unset=True)
        for key,value in user_data.items():
            setattr(current_user,key,value)
        session.add(current_user)
        session.commit()
        session.refresh(current_user)
        return current_user
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail=f"{e}" + "Something went wrong")

@private_user_router.get("/",response_model=list[UserResponse],status_code=HTTPStatus.OK)
def get_users(session:Session = Depends(get_session)):
    try:
        users = session.exec(select(User)).all()
        return users
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail=f"{e}" + "Something went wrong")


@private_user_router.get("/{id}",response_model=UserResponse,status_code=HTTPStatus.OK)
def get_user(id:str,session:Session = Depends(get_session)):
    try:
        user = session.get(User,id)
        return user
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail=f"{e}" + "Something went wrong")


@private_user_router.delete("/{id}",response_model=UserResponse,status_code=HTTPStatus.OK)
def delete_user(id:str,session:Session = Depends(get_session)):
    try:
        user_model = session.get(User,id)
        session.delete(user_model)
        session.commit()
        return user_model
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail=f"{e}" + "Something went wrong")