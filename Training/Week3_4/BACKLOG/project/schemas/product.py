
from pydantic import Field
from pydantic import BaseModel

class ProductBase(BaseModel):
    name:str
    price:float = Field(...,gt=0)
    stock:int = Field(...,ge=0)


class ProductRequest(ProductBase):
    pass

class ProductResponse(ProductBase):
    id:int
    is_active:bool
    
