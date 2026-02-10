from service.redis_service import get_redis_service
from sqlalchemy.ext.asyncio import AsyncSession
from service.redis_service import RedisService
from db.db_config import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from models.models import User
from schemas.products import ProductUpdate
from schemas.products import ProductCreate
from fastapi import HTTPException
from uuid import UUID
from repository.product_repository import ProductRepository
from service.base_service import BaseService
from models.models import Product


class ProductService(BaseService[Product]):
    def __init__(self, repository: ProductRepository,cache_service:RedisService):
        super().__init__(repository,cache_service)

    async def get_product_by_id(self, id: int):
        product = await self.repository.get_by_id(id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    async def get_product_by_name(self, name: str):
        return await self.repository.get_by_name(name)

    async def get_product_with_pagination(self, offset: int, limit: int):
        return await self.repository.get_by_pagination(offset, limit)

    async def get_all_products(self):
        return await self.repository.get_all()

    async def create_product(self, product: ProductCreate, current_user: User):
        if await self.get_product_by_name(product.name):
            raise HTTPException(status_code=400, detail="Product already exists")
        product_model = Product(**product.model_dump())
        product_model.user_id = current_user.id
        return await self.repository.create(product_model)

    async def delete_product(self, id: int, current_user: User):
        product = await self.get_product_by_id(id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        if product.user_id != current_user.id:
            raise HTTPException(
                status_code=403, detail="You are not authorized to delete this product"
            )
        return await self.repository.delete(product)

    async def update_product(self, product: ProductUpdate, id: int, current_user: User):
        product_model = await self.get_product_by_id(id)
        if not product_model:
            raise HTTPException(status_code=404, detail="Product not found")

        if product_model.user_id != current_user.id:
            raise HTTPException(
                status_code=403, detail="You are not authorized to update this product"
            )

        product_data = product.model_dump(exclude_unset=True)
        for key, value in product_data.items():
            setattr(product_model, key, value)
        return await self.repository.update(product_model)


def get_product_service(session: AsyncSession = Depends(get_session),cache_service:RedisService = Depends(get_redis_service)):
    return ProductService(ProductRepository(session),cache_service)
