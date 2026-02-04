from repository.base_repository import BaseRepository
from models.models import User
from sqlmodel import Session

class UserRepository(BaseRepository[User]):
    def __init__(self,session:Session):
        super().__init__(User,session)
    
    def get_by_email(self,email:str):
        return self.session.query(self.model_type).filter(self.model_type.email == email).first()
