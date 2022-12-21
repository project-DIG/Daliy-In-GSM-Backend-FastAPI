from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from core.config import settings

engine = create_engine(f"mysql+pymysql://{settings.DB_URL}")


def get_db():
    session = scoped_session(sessionmaker(bind=engine, autocommit=True))
    try:
        yield session
    finally:
        session.close()
