from db.db_config import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from models.models import User
from schemas.products import ProductUpdate
from schemas.products import ProductCreate
from fastapi import HTTPException
from uuid import UUID
from repository.product_repository import ProductRepository
from service.base_service import BaseService
from models.models import Product

class ProductService(BaseService[Product]):
    def __init__(self,repository:ProductRepository):
        super().__init__(repository)


    def get_product_by_id(self,id:str):
        product = self.repository.get_by_id(UUID(id))
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product


    def get_product_by_name(self,name:str):
        return self.repository.get_by_name(name)


    def get_product_with_pagination(self,offset:int,limit:int):
        return self.repository.get_by_pagination(offset,limit)
    
    def get_all_products(self):
        return self.repository.get_all()
    
    def create_product(self,product:ProductCreate,current_user:User):
        if self.get_product_by_name(product.name):
            raise HTTPException(status_code=400, detail="Product already exists")
        product_model = Product(**product.model_dump())
        product_model.user_id = current_user.id
        return self.repository.create(product_model)
    
    def delete_product(self,id:str,current_user:User):
        product = self.get_product_by_id(id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        if product.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="You are not authorized to delete this product")
        return self.repository.delete(product)
    
    def update_product(self,product:ProductUpdate,id:str,current_user:User):
        product_model = self.get_product_by_id(id)
        if not product_model:
            raise HTTPException(status_code=404, detail="Product not found")

        if product_model.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="You are not authorized to update this product")

        product_data = product.model_dump(exclude_unset=True)
        for key, value in product_data.items():
            setattr(product_model, key, value)
        return self.repository.update(product_model)



def get_product_service(session:Session = Depends(get_session)):
    return ProductService(ProductRepository(session))