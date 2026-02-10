from repository.base_repository import BaseRepository
from models.models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class ProductRepository(BaseRepository[Product]):
    def __init__(self, session: AsyncSession):
        super().__init__(Product, session)

    async def get_by_name(self, name: str):
        result = await self.session.execute(select(self.model_type).where(self.model_type.name == name))
        return result.scalars().first()
