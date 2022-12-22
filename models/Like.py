from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)
    video_id = Column(ForeignKey("video.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)
    type = Column(String(45), nullable=False)

    user = relationship("User")
    video = relationship("Video")
