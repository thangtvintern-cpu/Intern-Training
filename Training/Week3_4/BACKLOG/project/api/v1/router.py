from fastapi import APIRouter
from api.v1.products import router as products_router

router = APIRouter(prefix="/api/v1",tags=["v1"])
router.include_router(products_router)