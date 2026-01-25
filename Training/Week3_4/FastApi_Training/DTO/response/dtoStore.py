
from pydantic import BaseModel,Field

class Attribute(BaseModel):
    name01: str | None = Field(default=None,description = "Tên vé")
    price01: int | None = Field(default=None,ge = 0,description = "Giá vé của name 01")
    value01: int | None = Field(default=None,ge = 0,description = "Số lượng vé")
    name02: str | None = Field(default=None,description = "Tên vé")
    price02: int | None = Field(default=None,ge = 0,description = "Giá vé của name 02")
    value02: int | None = Field(default=None,ge = 0,description = "Số lượng vé")
    name03: str | None = Field(default=None,description = "Tên vé")
    price03: int | None = Field(default=None,ge = 0,description = "Giá vé của name 03")
    value03: int | None = Field(default=None,ge = 0,description = "Số lượng vé")

class Purchase(BaseModel):
    purchase_id: str = Field(...,alias='purchaseId',description="Id của đơn hàng")
    package_id: str = Field(...,alias = 'packageId',description="Id của gói vé")
    tenant_id: str | None = Field(default=None,description="Id của khách hàng")
    purchase_at: str = Field(...,alias = 'purchaseAt',description="Thời gian mua vé")
    stock_category: str = Field(...,alias = 'stockCategory',description="Loại vé")
    attribute: Attribute = Field(...,alias = 'attribute',description="Thông tin vé")
    assign_point: int = Field(...,alias = 'assignPoint',ge = 0,description="Điểm được trao")
    point: int = Field(...,alias = 'point',ge = 0,description="Điểm hiện tại")
    have_value: int = Field(...,alias = 'haveValue',ge = 0,description="Tổng số lượng vé")
    model_config = {
        'populate_by_name': True    
    }

class User(BaseModel):
    user_id: str
    purchase: list[Purchase]

