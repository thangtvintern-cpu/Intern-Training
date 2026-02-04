
from sqlalchemy.orm import Session
from typing import TypeVar,Type,Generic


ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self,model_type:Type[ModelType],session:Session):
        self.model_type = model_type
        self.session = session


    def get_by_pagination(self,offset:int,limit:int):
        return self.session.query(self.model_type).offset(offset).limit(limit).all()


    def get_all(self):
        return self.session.query(self.model_type).all()


    def get_by_id(self,id):
        return self.session.get(self.model_type,id)

    
    def create(self,model:ModelType):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model


    def delete(self,model:ModelType):
        self.session.delete(model)
        self.session.commit()
        return model


    def update(self,model:ModelType):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model
    