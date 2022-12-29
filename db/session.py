from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import redis
from core.config import settings

engine = create_engine(f"mysql+pymysql://{settings.DB_URL}")


def get_db():

    try:
        session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
        yield session
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()


def get_redis_db():
    try:
        conn = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
        yield conn
    except Exception as e:
        print(e)
    finally:
        conn.close()
