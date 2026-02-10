
from core.config import AppSettings
from typing import Optional
from redis.asyncio import Redis
from functools import lru_cache

redis_client : Optional[Redis] = None
settings = AppSettings()
def get_redis_client():
    global redis_client
    if redis_client is None:
        redis_client = Redis.from_url(settings.REDIS_URL, decode_responses=True)
    return redis_client

def close_redis_client():
    global redis_client
    if redis_client is not None:
        redis_client.close()
        redis_client = None

@lru_cache
def get_redis():
    return get_redis_client()