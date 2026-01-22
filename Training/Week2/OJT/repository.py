from copy import copy
from datetime import datetime
import json
import pickle



# Giả lập repository
class UserPurchaseRepo:
    remake_data = None
    type_dict_of_data = None

    def __init__(self,path):
        if path.endswith('.pkl') != True:
            raise Exception('Path must end with .pkl')  
        reader = open(path,'rb')
        # Lấy ra dữ liệu từ file
        data = pickle.load(reader)
        reader.close()

        # refactor data (thêm have_value, point, assign_point)
        self.remake_data = self.__refactor_data(data)
        # Tạo ra dictionary theo user_id
        self.type_dict_of_data = {purchase['user_id']:purchase for purchase in self.remake_data}  
        

    def getAllUserPurchase(self) -> dict:
        dict = {}
        dict['users'] = self.remake_data
        dict['timestamp'] = datetime.now().timestamp()
        return dict

    # refactor data
    def __refactor_data(self,data:list) -> list:
        dedup_data = set()
        for purchase in data:
            count = 1
            haveValue = 0
            attr = purchase.get('attribute', {})
            while True:
                value = attr.get(f"value{count:02}")
                if value is None:
                    break
                haveValue += value
                count += 1
            purchase['have_value'] = haveValue

            purchase_id = purchase.get('purchase_id')
            if purchase_id in dedup_data:
                purchase['point'] = 0
                purchase['assign_point'] = 0
            else:
                dedup_data.add(purchase_id)
        return data

    def getUserById(self, user_id) -> dict:
        print(self.type_dict_of_data.get(user_id))
        return self.type_dict_of_data.get(user_id)

def get_repo(path):
    return UserPurchaseRepo(path)    




   