
from fastapi import FastAPI
from api.endpoint.users import router as users_router
from api.endpoint.purchases import router as purchases_router

app = FastAPI()
app.include_router(users_router)
app.include_router(purchases_router)


