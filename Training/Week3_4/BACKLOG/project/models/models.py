from datetime import datetime
from sqlmodel import SQLModel,Field

class Product(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    name:str = Field(...,max_length=100)
    price:float = Field(...,gt=0)
    stock:int = Field(...,ge=0)
    is_active:bool = Field(default=True)
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:datetime = Field(default_factory=datetime.now)
