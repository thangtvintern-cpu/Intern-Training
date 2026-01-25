from DTO.response.dtoStore import Attribute
from pydantic import BaseModel,Field


class CreatePurchaseByUserId(BaseModel):
    user_id: str = Field(...,alias='userId')
    attribute: Attribute = Field(...,alias='attribute') 