from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import redis
from core.config import settings

engine = create_engine(f"mysql+pymysql://{settings.DB_URL}")


def get_db():
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    try:
        yield session
        session.commit()
    finally:
        session.close()


def get_redis_db():
    conn = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
    try:
        yield conn
    finally:
        conn.close()
