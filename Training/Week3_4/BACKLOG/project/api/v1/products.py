from uuid import UUID
from fastapi import Query
from typing import Annotated
from schemas.products import Pagination
from core.security import get_current_user
from models.models import User
from fastapi import HTTPException
from schemas.products import ProductUpdate
from schemas.products import ProductCreate
from http import HTTPStatus
from sqlmodel import select
from db.db_config import get_session
from sqlalchemy.orm import Session
from core.security import verify_token
from fastapi import Depends
from fastapi import APIRouter
from schemas.products import ProductResponse
from models.models import Product

public_product_router = APIRouter(prefix="/products",tags=["v1 - products"])
private_product_router = APIRouter(prefix="/products",dependencies=[Depends(verify_token)],tags=["v1 - products"])


# Public Endpoints
@public_product_router.get("/",response_model=list[ProductResponse],status_code=HTTPStatus.OK)
def get_all_products(pagination:Annotated[Pagination,Query()],
session:Session = Depends(get_session)):
    try:
        return session.exec(select(Product).order_by(Product.price.asc()).offset(pagination.offset).limit(pagination.limit)).all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail="Something went wrong when querying all products")



@public_product_router.get("/{id}",response_model=ProductResponse,status_code=HTTPStatus.OK)
def get_product_by_id(id:str,session:Session = Depends(get_session)):
    try:
        product_model = session.get(Product,UUID(id))
        if not product_model:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail="Product not found")
        return product_model
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail="Something went wrong when querying a product")



#------------------------------------------------------------------------------------------------------------------


# Private Endpoints
@private_product_router.post("/",response_model=ProductResponse,status_code=HTTPStatus.CREATED)
def create_product(product:ProductCreate,
session:Session = Depends(get_session),
current_user:User = Depends(get_current_user)):
    try:
        product_model = Product(**product.model_dump(exclude_unset=True))
        current_user.products.append(product_model)
        session.add(current_user)
        session.commit()
        session.refresh(current_user)
        return product_model
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Something went wrong when creating a product")


@private_product_router.put("/{id}",status_code=HTTPStatus.OK)
def update_product(id:str,product_update:ProductUpdate,session:Session = Depends(get_session)):
    try:
        product_model = session.get(Product,UUID(id))
        if not product_model:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail="Product not found")
        for k,v in product_update.model_dump(exclude_unset=True).items():
            setattr(product_model,k,v)
        session.add(product_model)
        session.commit()
        session.refresh(product_model)
        return product_model
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail="Something went wrong when updating a product")


@private_product_router.delete("/{id}",status_code=HTTPStatus.OK)
def delete_product(id:str,session:Session = Depends(get_session)):
    try:
        product_model = session.get(Product,UUID(id))
        if not product_model:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail="Product not found")
        session.delete(product_model)
        session.commit()
        return {"message":"Product deleted successfully"}
    except Exception as e:  
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail="Something went wrong when deleting a product")

        