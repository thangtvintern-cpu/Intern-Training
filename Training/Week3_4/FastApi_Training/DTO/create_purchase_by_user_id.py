from pydantic import field_serializer
from datetime import datetime
from DTO.dto_store import Attribute
from pydantic import BaseModel,Field


class CreatePurchaseByUserIdRequest(BaseModel):
    user_id: str = Field(...,alias='userId')
    attribute: Attribute = Field(...,alias='attribute')
    model_config = {
        'populate_by_name': True,
        'example':{
            'userId':'123',
            'attribute':{
                'name01':'大人',
                'price01':123,
                'value01':123,
                'name02':'子供',
                'price02':123,
                'value02':123,
                'name03':'ベビ',
                'price03':123,
                'value03':123
            }
        }   
    }


class CreatePurchaseByUserIdResponse(BaseModel):
    user_id: str = Field(...,alias='userId')
    purchase_id: str = Field(...,alias='purchaseId')
    purchase_at: datetime = Field(default_factory=datetime.now)
    @field_serializer('purchase_at')
    def serialize_purchase_at(self, dt:datetime):
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    model_config = {
        'populate_by_name': True,
        'example':{
            'userId':'123',
            'purchaseId':'123',
            'purchase_at':'2022-01-01'
        }   
    }
