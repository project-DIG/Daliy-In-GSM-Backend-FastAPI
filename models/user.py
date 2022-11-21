from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TINYTEXT
from db.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, comment='아이디')
    nickname = Column(String(45), nullable=False, comment='닉네임')
    image_url = Column(TINYTEXT, nullable=False, comment='이미지 url')
    email = Column(String(45), nullable=False, comment='이메일')
    bio = Column(TINYTEXT, nullable=False, comment='자기소개')