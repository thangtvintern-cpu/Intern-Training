from pydantic import Field
from pydantic import BaseModel
from pydantic import EmailStr

class CreateUserBase(BaseModel):
    name:str = Field(...,min_length=7,max_length=25)
    email:EmailStr = Field(...)

class CreateUserRequest(CreateUserBase):
    password:str = Field(...,min_length=7,max_length=25)

class CreateUserResponse(CreateUserBase):
    id:str = Field(...)
    refresh_token:str = Field(...)
    access_token:str = Field(...)
