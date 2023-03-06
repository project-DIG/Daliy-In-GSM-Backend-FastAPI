from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    DB_URL: str = os.getenv("DB_URL")

    REDIS_HOST: str = "redis"

    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITM: str = "HS256"

    REFRESH_EXPIRE: int = 604800  # 1주
    ACCESS_EXPIRE: int = 1800  # 30분
    EMAIL_AUTH_EXPIRE: int = 300  # 5분


settings = Settings()
