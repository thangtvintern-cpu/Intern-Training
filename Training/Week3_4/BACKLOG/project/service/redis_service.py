from pydantic import BaseModel
import json
from typing import Any
from typing import Optional
from redis.asyncio import Redis
from db.redis import get_redis
from fastapi import Depends


class RedisService:
    def __init__(self, redis: Redis):
        self.redis = redis

    def __serialize_data(self, data: Any):
        if isinstance(data, list):
            return json.dumps([
                item.model_dump(mode="json") if hasattr(item, "model_dump") else item
                for item in data
            ])
        if hasattr(data, "model_dump"):
            return json.dumps(data.model_dump(mode="json"))

        return json.dumps(data)

    async def add_to_cache(self, key: str, value: Any, ex: int = 60 * 3):
        await self.redis.set(key, self.__serialize_data(value), ex=ex)
        print(f"Added to cache: {key}")

    async def get_from_cache(self, key: str):
        result = await self.redis.get(key)
        print(f"Got from cache: {result}")
        return json.loads(result) if result else None

    async def exists_in_cache(self, key: str):
        return await self.redis.exists(key)


    async def delete_from_cache(self, key: str):
        await self.redis.delete(key)
    

    async def delete_pattern_cache(self,pattern:str):
        cursor = 0
        while True:
            cursor,keys = await self.redis.scan(cursor = cursor,match=pattern,count=50)
            if keys:
                await self.redis.delete(*keys)
            if cursor == 0:
                print(f"Deleted pattern cache: {pattern}")
                break


def get_redis_service(redis: Redis = Depends(get_redis)):
    return RedisService(redis)
