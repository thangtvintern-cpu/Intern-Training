from sqlalchemy.sql import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Type, Generic


ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self, model_type: Type[ModelType], session: AsyncSession):
        self.model_type = model_type
        self.session = session

    async def get_by_pagination(self, offset: int, limit: int):
        result = await self.session.execute(select(self.model_type).offset(offset).limit(limit))
        return result.scalars().all()

    async def get_all(self):
        result = await self.session.execute(select(self.model_type))
        return result.scalars().all()

    async def get_by_id(self, id):
        result = await self.session.get(self.model_type, id)
        return result

    async def create(self, model: ModelType):
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model

    async def delete(self, model: ModelType):
        self.session.delete(model)
        await self.session.commit()
        return model

    async def update(self, model: ModelType):
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model
