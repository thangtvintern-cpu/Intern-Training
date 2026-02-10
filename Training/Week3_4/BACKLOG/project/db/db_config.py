from schemas.user import UserRole
from core.hash import get_password_hash
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.sql import select
from sqlmodel import SQLModel
from core.config import AppSettings
from models.models import User
settings = AppSettings()

engine = create_async_engine(settings.DATABASE_URL,connect_args={"check_same_thread":False})

async def get_session():
    async with AsyncSession(engine) as session:
        yield session


async def create_db_and_table():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    if SQLModel.metadata.tables:
        async with AsyncSession(engine) as session:
            result = await session.execute(select(User).where(User.email == "weedkhalifa1608@gmail.com"))
            existing_user = result.scalars().first()
            if existing_user:
                return
            user = User(
                email= "weedkhalifa1608@gmail.com",
                password= get_password_hash("Tranthang97"),
                role= UserRole.ADMIN,
                name = "thang",
                mobile = "0123456789",
                age = 27
            )
            session.add(user)
            await session.commit()
        return
    