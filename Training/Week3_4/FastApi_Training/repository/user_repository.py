
from IPython.utils.py3compat import encode
from prompt_toolkit.key_binding.bindings.named_commands import end_kbd_macro
from functools import lru_cache
import json
from pathlib import Path
import uuid

BASE_DIR = Path(__file__).resolve().parent
path = str(BASE_DIR / "data_user.json")

class UserRepository:
    def __init__(self):
        self.file_path = path


    def __write_file(self, data):
        old_data = self.__read_file()
        old_data.append(data)
        with open(self.file_path, 'w',encoding='utf-8') as f:
            json.dump(old_data,f,indent=2,ensure_ascii=False)

    def __read_file(self):
        with open(self.file_path, 'r',encoding='utf-8') as f:
            return json.load(f)


    def get_all_user(self):
        data = self.__read_file()
        return data

    def get_user_by_id(self, user_id):
        data = self.get_all_user()
        for user in data:
            if user.get('id') == user_id:
                return user

    def get_user_by_email(self, email):
        data = self.get_all_user()
        for user in data:
            if user.get('email') == email:
                return user
        return None
    def login(self, user) -> bool:
        data = self.get_user_by_email(user['email'])
        if data is None:
            return False
        if data['password'] == user['password']:
            return True


    def create_user(self, user):
        if self.get_user_by_email(user['email']) is not None:
            return False
        data = self.get_all_user()
        user['id'] = str(uuid.uuid4())
        user['refresh_token'] = "Bearer " + str(uuid.uuid4())
        user['access_token'] = "Bearer " + str(uuid.uuid4())
        data.append(user)
        self.__write_file(data)
        return True
    
    def check_auth(self, access_token):
        data = self.get_all_user()
        for user in data:
            if user['access_token'] == access_token:
                return True
        return False
    
@lru_cache(maxsize=None)
def get_user_repository():
    return UserRepository()