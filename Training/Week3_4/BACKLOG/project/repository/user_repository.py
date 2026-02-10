from sqlalchemy.sql import select
from repository.base_repository import BaseRepository
from models.models import User
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_email(self, email: str):
        result = await self.session.execute(select(self.model_type).where(self.model_type.email == email))
        return result.scalars().first()
    
    async def exists_by_email(self, email: str):
        result = await self.session.execute(select(self.model_type).where(self.model_type.email == email))
        return result.scalars().first() is not None
    
