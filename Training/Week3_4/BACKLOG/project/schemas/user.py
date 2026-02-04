from uuid import UUID
from datetime import datetime
from pydantic import EmailStr
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import field_validator
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class UserCreate(BaseModel):
    name: str
    email: EmailStr = Field(..., unique=True)
    password: str
    confirm_password: str
    age: int = Field(..., gt=0, lt=120)
    mobile: str = Field(..., min_length=10, max_length=10)

    @field_validator("confirm_password")
    def validate_confirm_password(cls, v, info):
        if v != info.data.get("password"):
            raise ValueError("Passwords do not match")
        return v


class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    age: Optional[int] = Field(default=None, gt=0, lt=120)
    mobile: Optional[str] = Field(default=None, min_length=10, max_length=10)


class UserResponse(BaseModel):
    id: UUID
    name: str | None
    email: EmailStr
    age: int | None
    mobile: str | None
    is_active: bool
    role: UserRole
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = {
        "from_attributes": True,
    }
