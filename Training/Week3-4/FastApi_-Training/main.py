from fastapi import FastAPI
from repository.repository import get_repo

app = FastAPI()
repo = get_repo()

@app.get('/hello')
def hello():
    return {'message': 'Hello World'}


@app.get('/purchases')
def get_all_users():
    return repo.getAllData()

@app.get('/purchases/{user_id}')
def get_user(user_id:str):
    return repo.get_all_purchase_by_user_id(user_id)

@app.get('/purchases/{user_id}/total-price')
def get_total_price_by_user_id(user_id:str):
    return {'all_purchases_total_price':repo.get_total_price_by_user_id(user_id)}


@app.get('/purchases/{user_id}/total-price/{purchase_id}')
def get_total_price_by_user_id_and_purchase_id(user_id:str,purchase_id:str):
    return {'purchase_total_price':repo.get_total_price_by_user_id_and_purchase_id(user_id,purchase_id)}