from main import app
from db.session import get_db, get_redis_db, engine
from sqlalchemy.orm import Session
import fakeredis


def override_get_db():
    session = Session(bind=engine)
    try:
        yield session
        session.rollback()
    finally:
        session.close()


def override_get_redis_db():
    conn = fakeredis.FakeStrictRedis()
    try:
        yield conn
    finally:
        conn.close()


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_redis_db] = override_get_redis_db
