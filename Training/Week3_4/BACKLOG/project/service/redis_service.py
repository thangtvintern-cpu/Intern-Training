from typing import Any
from typing import Optional
from redis.asyncio import Redis
from db.redis import get_redis
from fastapi import Depends


class RedisService:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def add_to_cache(self, key: str, value: Any, ttl: int = 60 * 3):
        await self.redis.set(key, value, ex=ttl)

    async def get_from_cache(self, key: str):
        return await self.redis.get(key)

    async def exists_in_cache(self, key: str):
        return await self.redis.exists(key)


def get_redis_service(redis: Redis = Depends(get_redis)):
    return RedisService(redis)
