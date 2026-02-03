from api.v1.products import private_product_router,public_product_router
from fastapi import APIRouter
from api.v1.users import public_user_router,private_user_router
from api.v1.auth import public_auth_router,private_auth_router 


router = APIRouter(prefix="/api/v1")
router.include_router(public_user_router)
router.include_router(private_user_router)
router.include_router(public_auth_router)
router.include_router(private_auth_router)
router.include_router(public_product_router)
router.include_router(private_product_router)
