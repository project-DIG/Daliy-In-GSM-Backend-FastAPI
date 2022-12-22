from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TINYTEXT
from sqlalchemy.ext.declarative import declarative_base
from db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    password = Column(TINYTEXT)
    email = Column(String(45))
    profile_image = Column(TINYTEXT)
