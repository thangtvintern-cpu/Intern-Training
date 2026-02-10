import asyncio
from typing import Callable
from functools import wraps

concurrent_request = {}
_lock = asyncio.Lock()

def cache_checker(key_builder: Callable[..., str], ttl: int = 60 * 5):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            key = key_builder(*args, **kwargs)
            cached_value = await self.cache_service.get_from_cache(key)
            if cached_value:
                print(f"Cache hit rồi : {key}")
                return cached_value
            
            print(f"Cache miss rồi : {key}")

            async with _lock:
                if key in concurrent_request:
                    future = concurrent_request[key]
                    is_querier = False
                else:
                    future = asyncio.Future()
                    concurrent_request[key] = future
                    is_querier = True
            
            if not is_querier:
                return await future.result()
            else:
                try:
                    result = await func(self, *args, **kwargs)
                    await self.cache_service.add_to_cache(key, result, ex=ttl)
                    future.set_result(result)
                    return result
                finally:
                    del concurrent_request[key]

        return wrapper
    return decorator


def cache_validator(pattern: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            result = await func(self, *args, **kwargs)
            await self.cache_service.delete_pattern_cache(pattern)
            return result
        return wrapper
    return decorator