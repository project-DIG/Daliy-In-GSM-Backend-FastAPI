from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TINYINT, TINYTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.base import Base


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    commentor_id = Column(ForeignKey('user.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    target_id = Column(ForeignKey('clip.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    depth = Column(TINYINT, nullable=False)

    commentor = relationship('User')
    target = relationship('Clip')