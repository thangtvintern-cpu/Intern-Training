
from pydantic import Field
from pydantic import EmailStr
from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: EmailStr = Field(...,description="Email của user")
    password: str = Field(...,description="password của email")


class LoginResponse(BaseModel):
    access_token : str
    refresh_token : str