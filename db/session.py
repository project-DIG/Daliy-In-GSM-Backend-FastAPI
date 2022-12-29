from sqlalchemy import create_engine
from fastapi import HTTPException, status
from sqlalchemy.orm import scoped_session, sessionmaker
from core.config import settings
import redis

engine = create_engine(f"mysql+pymysql://{settings.DB_URL}")


def get_db():

    try:
        session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
        yield session
        session.commit()
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=e)
    finally:
        session.close()


def get_redis_db():
    try:
        conn = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
        yield conn
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=e)
    finally:
        conn.close()
