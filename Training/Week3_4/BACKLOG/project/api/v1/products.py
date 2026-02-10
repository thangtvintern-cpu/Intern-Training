from service.product_service import get_product_service, ProductService
from fastapi import Query
from typing import Annotated
from schemas.common import Pagination
from core.security import get_current_user, parse_token
from models.models import User
from schemas.products import ProductUpdate
from schemas.products import ProductCreate
from http import HTTPStatus
from fastapi import Depends
from fastapi import APIRouter
from schemas.products import ProductResponse


public_product_router = APIRouter(prefix="/products", tags=["v1 - products"])
private_product_router = APIRouter(
    prefix="/products", dependencies=[Depends(parse_token)], tags=["v1 - products"]
)


# Public Endpoints
@public_product_router.get(
    "/", response_model=list[ProductResponse], status_code=HTTPStatus.OK
)
async def get_products_pagination(
    pagination: Annotated[Pagination, Query()],
    product_service: ProductService = Depends(get_product_service),
):
    return product_service.get_product_with_pagination(
        pagination.offset, pagination.limit
    )


@public_product_router.get(
    "/all", response_model=list[ProductResponse], status_code=HTTPStatus.OK
)
async def get_all_products(product_service: ProductService = Depends(get_product_service)):
    return product_service.get_all_products()


@public_product_router.get(
    "/{id}", response_model=ProductResponse, status_code=HTTPStatus.OK
)
async def get_product_by_id(
    id: int, product_service: ProductService = Depends(get_product_service)
):
    return product_service.get_product_by_id(id)


# ------------------------------------------------------------------------------------------------------------------


# Private Endpoints


@private_product_router.post(
    "/", response_model=ProductResponse, status_code=HTTPStatus.CREATED
)
async def create_product(
    product: ProductCreate,
    product_service: ProductService = Depends(get_product_service),
    current_user: User = Depends(get_current_user),
):
    return product_service.create_product(product, current_user)


@private_product_router.put("/{id}", status_code=HTTPStatus.OK)
async def update_product(
    id: int,
    product_update: ProductUpdate,
    current_user: User = Depends(get_current_user),
    product_service: ProductService = Depends(get_product_service),
):
    return product_service.update_product(product_update, id, current_user)


@private_product_router.delete("/{id}", status_code=HTTPStatus.OK)
async def delete_product(
    id: int,
    current_user: User = Depends(get_current_user),
    product_service: ProductService = Depends(get_product_service),
):
    return product_service.delete_product(id, current_user)
