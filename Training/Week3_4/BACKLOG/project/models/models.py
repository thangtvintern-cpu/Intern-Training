
from sqlalchemy import UUID
from typing import Optional
from uuid import uuid4,UUID
from datetime import datetime
from sqlmodel import SQLModel,Field

class BaseModel(SQLModel):
    id: UUID = Field(
        default_factory= uuid4,
        primary_key=True,
        nullable=False
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False
    )
    updated_at: Optional[datetime] = Field(
        default=None
    )


class User(BaseModel,table=True):
    __tablename__ = "users"
    email: str = Field(
        nullable=False,
        unique=True
    )
    name: str = Field(
        nullable=True
    )
    age: int = Field(
        nullable=True
    )
    mobile: str = Field(
        nullable=True
    )
    password: str = Field(
        nullable=False
    )
    is_active: bool = Field(
        default=True
    )
    role : str = Field(
        default="user",
        nullable=False
    )


