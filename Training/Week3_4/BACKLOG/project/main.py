
from db.redis import get_redis
from core.config import get_settings
from core.exceptions import register_exception_handler
from db.db_config import create_db_and_table
from fastapi import FastAPI
from api.v1.router import router as v1_router

app = FastAPI()
app.include_router(v1_router)

@app.on_event("startup")
async def startup_event():
    await create_db_and_table()

register_exception_handler(app)
settings = get_settings()
@app.get("/")
def hello_world():
    return {"message": "Welcome to the Product API"}



# @app.on_event("startup")
# async def test_redis():
#     redis = get_redis()
#     print("Redis is running: ",await redis.ping())


