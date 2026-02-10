from sqlalchemy import Column
from sqlmodel import Relationship
from sqlalchemy import UUID
from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime
from sqlmodel import SQLModel, Field
from schemas.user import UserRole


class BaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: Optional[datetime] = Field(default=None)


class User(BaseModel, table=True):
    __tablename__ = "users"
    email: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=True)
    age: int = Field(nullable=True)
    mobile: str = Field(nullable=True)
    password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    role: UserRole = Field(default="user", nullable=False)
    products: list["Product"] = Relationship(back_populates="user")


class Product(BaseModel, table=True):
    __tablename__ = "products"
    name: str = Field(nullable=False, unique=True)
    price: int = Field(nullable=False)
    stock: int = Field(nullable=False)
    description: str = Field(nullable=True)
    is_active: bool = Field(default=True)
    user_id: UUID = Field(nullable=False, foreign_key="users.id")
    user: "User" = Relationship(back_populates="products")
