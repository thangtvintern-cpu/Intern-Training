from schemas.user import UserRole
from core.hash import get_password_hash
from sqlmodel import create_engine,Session,SQLModel,select
from core.config import DATABASE_URL
from models.models import User

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_table():
    SQLModel.metadata.create_all(engine)
    if SQLModel.metadata.tables:
        with Session(engine) as session:
            existing_user = session.exec(select(User).where(User.email == "weedkhalifa1608@gmail.com")).first()
            if existing_user:
                return
            user = User(
                email= "weedkhalifa1608@gmail.com",
                password= get_password_hash("Tranthang97"),
                role= UserRole.ADMIN
            )
            session.add(user)
            session.commit()
        return
    