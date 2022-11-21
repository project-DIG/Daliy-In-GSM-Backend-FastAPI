from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TINYTEXT
from sqlalchemy.orm import relationship
from db.base import Base

class Clip(Base):
    __tablename__ = 'clip'

    id = Column(Integer, primary_key=True, comment='아이디')
    title = Column(String(45), nullable=False, comment='제목')
    streamer_name = Column(String(45), nullable=False, comment='스트리머 이름')
    description = Column(TINYTEXT, nullable=False, comment='설명')
    upload_date = Column(DateTime, nullable=False, comment='업로드 날짜')
    views = Column(Integer, nullable=False, comment='조회수')
    uploader_id = Column(ForeignKey('user.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='업로더 아이디')

    uploader = relationship('User')