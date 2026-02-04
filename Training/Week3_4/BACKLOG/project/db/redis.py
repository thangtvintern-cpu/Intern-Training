
from redis.asyncio import Redis
from core.config import REDIS_URL
from functools import lru_cache

redis = Redis.from_url(REDIS_URL, decode_responses=True)


@lru_cache
def get_redis():
    return redis