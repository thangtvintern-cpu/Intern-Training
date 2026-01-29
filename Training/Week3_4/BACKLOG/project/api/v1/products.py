from fastapi import Depends
from fastapi import APIRouter
from schemas.product import ProductRequest,ProductResponse
from db.db_config import get_session
from sqlmodel import Session
from models.models import Product

router = APIRouter(prefix="/products",tags=["products"])

@router.post("/",response_model=ProductResponse)
def create_product(product:ProductRequest,session:Session = Depends(get_session)):
    product_model = Product.from_orm(product)
    session.add(product_model)
    session.commit()
    session.refresh(product_model)
    return product_model
