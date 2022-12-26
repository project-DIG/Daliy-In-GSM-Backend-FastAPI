from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    video_id = Column(ForeignKey("video.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)
    commenter_id = Column(ForeignKey("user.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)
    content = Column(String(45), nullable=False)
    like = Column(Integer, nullable=False)

    commenter = relationship("User")
    video = relationship("Video")
