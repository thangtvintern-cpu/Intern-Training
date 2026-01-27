

from DTO.dto_store import User
from fastapi import Query
from core.security.check_auth import check_auth
from fastapi import Header
from DTO.create_purchase_by_user_id import CreatePurchaseByUserIdRequest
from typing import Annotated
from fastapi import Body
from DTO.create_purchase_by_user_id import CreatePurchaseByUserIdResponse
from repository.repository import get_repo
from fastapi import APIRouter

router = APIRouter(prefix="/purchases", tags=['purchases'])

repo = get_repo()


@router.post('/create-purchase',response_model=CreatePurchaseByUserIdResponse)
def create_purchase_by_user_id(access_token:Annotated[str,Header()] ,req:Annotated[CreatePurchaseByUserIdRequest,Body(embed=True)]
    ):
    if not check_auth(access_token):
        return {'message':'Unauthorized'}
    return repo.create_purchase_by_user_id(req.user_id,req.attribute)


@router.get('/{user_id}',response_model=User)
def get_all_purchase_by_user_id(
    access_token:Annotated[str,Header()],
    user_id:str,
    skip : Annotated[int,Query(ge=0,title='skip',description='lấy từ phần tử nào')]= 0,
    limit : Annotated[int | None,Query(le=20,title='limit',description='lấy bao nhiêu phần tử')]= None,
    ):
    if not check_auth(access_token):
        return {'message':'Unauthorized'}
    return {'user_id':user_id,'purchase': repo.get_all_purchase_by_user_id(user_id,skip,limit)}



@router.get('/{user_id}/total-price')
def get_total_price_by_user_id(user_id:str):
    return {'all_purchases_total_price':repo.get_total_price_by_user_id(user_id)}


@router.get('/{user_id}/total-price/{purchase_id}')
def get_total_price_by_user_id_and_purchase_id(user_id:str,purchase_id:str):
    return {'purchase_total_price':repo.get_total_price_by_user_id_and_purchase_id(user_id,purchase_id)}


@router.get('')
def get_all_users():
    return repo.getAllData()