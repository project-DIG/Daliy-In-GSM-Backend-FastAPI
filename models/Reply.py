from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db.base import Base


class Reply(Base):
    __tablename__ = "reply"

    id = Column(Integer, primary_key=True)
    comment_id = Column(ForeignKey("comment.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)
    commenter_id = Column(ForeignKey("user.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)
    content = Column(Integer, nullable=False)
    like = Column(Integer, nullable=False)

    comment = relationship("Comment")
    commenter = relationship("User")
