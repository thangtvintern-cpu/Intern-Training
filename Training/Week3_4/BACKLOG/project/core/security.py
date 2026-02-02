import bcrypt
from uuid import UUID
from models.models import User
from db.db_config import get_session
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import Depends
from core.config import SECRET_KEY
from datetime import timedelta
from datetime import datetime
from pydantic import BaseModel
from bcrypt import hashpw,checkpw
from jose import JWTError,jwt
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer

security = HTTPBearer()
class TokenPayLoad(BaseModel):
    sub:str
    exp:int
    type:str
    role:str


def get_password_hash(password:str):
    return hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password:str,hashed_password:str):
    return checkpw(plain_password.encode("utf-8"),hashed_password.encode("utf-8"))


def create_access_token(
    sub:UUID,
    role:str,
    expires_delta: timedelta = timedelta(minutes=10)
):
    expires_at = datetime.utcnow() + expires_delta
    payload = {
        "sub":str(sub),
        "role":role,
        "type":"access",
        "exp":expires_at
    }

    return jwt.encode(payload,SECRET_KEY,algorithm="HS256")

def create_refresh_token(
    sub:UUID,
    role:str,
    expires_delta: timedelta = timedelta(days=7)
):
    expires_at = datetime.utcnow() + expires_delta
    payload = {
        "sub":str(sub),
        "role":role,
        "type":"refresh",
        "exp":expires_at
    }

    return jwt.encode(payload,SECRET_KEY,algorithm="HS256")


def parse_token(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
        return TokenPayLoad(**payload)
    except JWTError:
        return None

def verify_token(credentials:HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials,SECRET_KEY,algorithms=["HS256"])
        return True
    except JWTError:
        raise HTTPException(status_code=401,detail="Token không hợp lệ")

def get_current_user(credentials:HTTPAuthorizationCredentials = Depends(security),
    session:Session= Depends(get_session)
):
    if credentials is None:
        raise HTTPException(status_code=401,detail="Không có token trong request")
    payload = parse_token(credentials.credentials)
    if payload is None or payload.type != "access":
        raise HTTPException(status_code=401,detail="Token không hợp lệ")
    
    user = session.get(User,UUID(payload.sub))
    if user is None:
        raise HTTPException(status_code=401,detail="User không tồn tại")
    return user
