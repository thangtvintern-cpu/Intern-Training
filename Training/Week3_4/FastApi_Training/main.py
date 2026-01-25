from DTO.request.create_purchase_by_user_id import CreatePurchaseByUserId
from fastapi import FastAPI
from repository.repository import get_repo
from DTO.response.dtoStore import User,Purchase
app = FastAPI()
repo = get_repo()

@app.get('/')
def hello():
    return {'message': 'Hello World'}



@app.post('/purchases/create-purchase')
def create_purchase_by_user_id(body:CreatePurchaseByUserId):
    return repo.create_purchase_by_user_id(body.user_id,body.attribute)

@app.get('/purchases/{user_id}',response_model=User)
def get_all_purchase_by_user_id(user_id:str,skip : int = 0, limit : int | None = None):
    return {'user_id':user_id,'purchase': repo.get_all_purchase_by_user_id(user_id,skip,limit)}



@app.get('/purchases/{user_id}/total-price')
def get_total_price_by_user_id(user_id:str):
    return {'all_purchases_total_price':repo.get_total_price_by_user_id(user_id)}


@app.get('/purchases/{user_id}/total-price/{purchase_id}')
def get_total_price_by_user_id_and_purchase_id(user_id:str,purchase_id:str):
    return {'purchase_total_price':repo.get_total_price_by_user_id_and_purchase_id(user_id,purchase_id)}


@app.get('/purchases')
def get_all_users():
    return repo.getAllData()