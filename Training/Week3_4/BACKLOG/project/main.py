from db.db_config import create_db_and_table
from fastapi import FastAPI
from api.v1.router import router as v1_router

app = FastAPI()
app.include_router(v1_router)


@app.get("/")
def hello_world():
    return {"message": "Welcome to the Product API"}

create_db_and_table()

