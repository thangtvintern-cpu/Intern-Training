
from repository.base_repository import BaseRepository
from typing import TypeVar,Generic
from service.redis_service import RedisService

ModelType = TypeVar("ModelType")

class BaseService(Generic[ModelType]):
    def __init__(self,repository:BaseRepository[ModelType],cache_service:RedisService):
        self.repository = repository
        self.cache_service = cache_service


    