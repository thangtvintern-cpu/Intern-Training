from repository.base_repository import BaseRepository
from sqlmodel import Session
from typing import TypeVar,Generic

ModelType = TypeVar("ModelType")

class BaseService(Generic[ModelType]):
    def __init__(self,repository:BaseRepository[ModelType]):
        self.repository = repository


    