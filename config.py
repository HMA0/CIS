from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    SECRET_KEY: str = "change_me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = "sqlite:///./app.db"
    CORS_ORIGINS: str = "*"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
