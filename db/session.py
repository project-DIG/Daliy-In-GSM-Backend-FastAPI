from sqlalchemy import create_engine
from fastapi import HTTPException, status
from sqlalchemy.orm import scoped_session, sessionmaker
from core.config import settings
import redis

engine = create_engine(f"mysql+pymysql://{settings.DB_URL}")


def get_db():
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    try:
        yield session
        session.commit()
    finally:
        session.close()


def get_redis_db():
    conn = redis.StrictRedis(host=settings.REDIS_HOST)
    try:
        yield conn
    finally:
        conn.close()
