from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import Field
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: int = Field(..., gt=0)
    stock: int = Field(..., gt=0)
    description: Optional[str] = Field(default=None)
    model_config = {
        "examples": [
            {
                "name": "Product 1",
                "price": 100,
                "stock": 10,
                "description": "Product 1 description",
            }
        ]
    }



class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    price: Optional[int] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, gt=0)
    description: Optional[str] = Field(default=None)
    model_config = {
        "examples": [
            {
                "name": "Product 1",
                "price": 100,
                "stock": 10,
                "description": "Product 1 description",
            }
        ]
    }


class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    stock: int
    description: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = {
        "from_attributes": True,
    }
