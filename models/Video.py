from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TINYTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.base import Base


class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True)
    title = Column(String(45), nullable=False)
    video_url = Column(TINYTEXT, nullable=False)
    like = Column(Integer, nullable=False)
    dislike = Column(Integer, nullable=False)
    tag = Column(String(45), nullable=False)
    uploader_id = Column(ForeignKey("user.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)

    uploader = relationship("User")
