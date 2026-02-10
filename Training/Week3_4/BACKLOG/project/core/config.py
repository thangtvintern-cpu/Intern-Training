from functools import lru_cache
from pydantic_settings import BaseSettings    


class AppSettings(BaseSettings):
    DATABASE_URL: str
    
    REDIS_URL: str

    SECRET_KEY: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 5
    refresh_token_expire_minutes: int = 60 * 60 * 24 * 7

    model_config = {
        "env_file": ".env"
    }


@lru_cache
def get_settings():
    return AppSettings()