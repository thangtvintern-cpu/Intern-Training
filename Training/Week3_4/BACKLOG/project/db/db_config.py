from sqlmodel import create_engine,Session,SQLModel
from core.config import DATABASE_URL

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_table():
    SQLModel.metadata.create_all(engine)
