
from textwrap import indent
import json
from collections import defaultdict
import json
from datetime import datetime
import pickle



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

        # refactor data (thêm have_value, point, assign_point)
        self.remake_data = self.__refactor_data(data)
        # Tạo ra dictionary theo user_id
        #self.type_dict_of_data = {purchase['user_id']:purchase for purchase in self.remake_data}  
        
    # refactor data
    def __refactor_data(self,data:list) -> list:
        dedup_data = set()
        remade_data = defaultdict(list)
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
            remade_data[user_id].append(purchase)

        return [{"user_id":key,"purchase":value} for key,value in remade_data.items()]


    def getAllUserPurchase(self) -> dict:
        dict = {}
        dict['users'] = self.remake_data
        dict['timestamp'] = datetime.now().timestamp()
        return dict

    # def getUserById(self, user_id) -> dict:
    #     return self.type_dict_of_data.get(user_id)

    # def getTotalPriceByUserId(self,user_id) -> int:
    #     attribute = self.type_dict_of_data.get(user_id).get('attribute')
    #     totalPrice = 0 
    #     for i in range(1,4):
    #         currentValue = attribute.get(f'value{i:02}')
    #         currentPrice = attribute.get(f'price{i:02}')
    #         if currentValue is None or currentPrice is None:
    #             continue
    #         totalPrice += int(currentValue)*int(currentPrice)
    #     return totalPrice

def get_repo(path):
    return UserPurchaseRepo(path)    




   