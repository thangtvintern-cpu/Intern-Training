from repository import get_repo
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
path = str(BASE_DIR / "data_json.pkl")
repo = get_repo(path)

def convertToJson(dict) -> json:
    return json.dumps(dict,indent=4,default=str,ensure_ascii=False)

# Giả lập api
def get_all_user_purchase() -> json:
    return convertToJson(repo.getAllUserPurchase())

def get_user_by_id(user_id) -> dict:
    return repo.getUserById(user_id)

def get_total_price_by_user_id(user_id) -> int:
    return repo.getTotalPriceByUserId(user_id)

if __name__ == '__main__':
    c = open('api-reponse-2.json','w',encoding='utf-8')
    c.write(get_all_user_purchase())
    c.close()
    print(get_user_by_id('m6zc646sqc8akVQSnJfecq'))
    print(get_total_price_by_user_id('m6zc646sqc8akVQSnJfecq'))