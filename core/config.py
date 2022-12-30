from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")

    DB_URL: str = f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITM: str = "HS256"

    REFRESH_EXPIRE: int = 604800  # 1주
    ACCESS_EXPIRE: int = 1800  # 30분
    EMAIL_AUTH_EXPIRE: int = 300  # 5분


settings = Settings()
