from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TINYTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'comment': '유저 테이블'}

    id = Column(Integer, primary_key=True, comment='아이디')
    nickname = Column(String(45), nullable=False, comment='닉네임')
    image_url = Column(TINYTEXT, nullable=False, comment='이미지 url')
    email = Column(String(45), nullable=False, comment='이메일')
    bio = Column(TINYTEXT, nullable=False, comment='자기소개')
