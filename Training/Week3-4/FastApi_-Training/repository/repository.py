
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import pickle
from functools import lru_cache



# Giả lập repository
class UserPurchaseRepo:
    remake_data = None
    type_dict_of_data = None

    def __init__(self,path):
        if path.endswith('.pkl') != True:
            raise Exception('Path must end with .pkl')  
        reader = open(path,'rb')
        data = pickle.load(reader)
        reader.close()

        # refactor data (thêm have_value, point, assign_point,gom purchase theo user_id)
        self.remake_data = self.__refactor_data(data)
        
    # refactor data
    def __refactor_data(self,data:list) -> list:
        dedup_data = set()
        new_data = defaultdict(list)
        for purchase in data:
            # tính toán have_value
            totalValue = 0
            attribute = purchase.get('attribute', {})
            for i in range(1,4):
                value = attribute.get(f"value{i:02}")
                if value is None:
                    continue
                totalValue += value
            purchase['have_value'] = totalValue

            # tính lại point và assign_point
            purchase_id = purchase.get('purchase_id')
            if purchase_id in dedup_data:
                purchase['point'] = 0
                purchase['assign_point'] = 0
            else:
                dedup_data.add(purchase_id)

            # format lại purchased_date
            purchase['purchase_at'] = purchase['purchased_date'].strftime('%Y-%m-%d %H:%M:%S')
            del purchase['purchased_date']

            # gom purchase cùng user_id
            user_id = purchase['user_id']
            del purchase['user_id']
            new_data[user_id].append(purchase)

        self.type_dict_of_data = new_data
        return [{"user_id":key,"purchase":value} for key,value in new_data.items()]


    def getAllData(self) -> dict:
        dict = {}
        dict['users'] = self.remake_data
        dict['timestamp'] = datetime.now().timestamp()
        return dict

    def get_all_purchase_by_user_id(self,user_id:str) -> list:
        return self.type_dict_of_data.get(user_id,[])

    def get_total_price_by_user_id(self,user_id:str) -> int:
        total_price = 0
        for purchase in self.get_all_purchase_by_user_id(user_id):
            for i in range(1,4):
                value = purchase['attribute'].get(f'value{i:02}')
                price = purchase['attribute'].get(f'price{i:02}')
                if value is None or price is None:
                    continue
                total_price += value * price
        return total_price
    def get_total_price_by_user_id_and_purchase_id(self,user_id:str,purchase_id:str) -> int:
        total_price = 0
        for purchase in self.get_all_purchase_by_user_id(user_id):
            if purchase['purchase_id'] == purchase_id:
                for i in range(1,4):
                    value = purchase['attribute'].get(f'value{i:02}')
                    price = purchase['attribute'].get(f'price{i:02}')
                    if value is None or price is None:
                        continue
                    total_price += value * price
                break
        return total_price



BASE_DIR = Path(__file__).resolve().parent
path = str(BASE_DIR / "data_json.pkl")
@lru_cache(maxsize=None)
def get_repo():
    return UserPurchaseRepo(path)    




   