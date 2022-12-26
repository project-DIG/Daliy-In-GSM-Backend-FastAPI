from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.base import Base


class Follow(Base):
    __tablename__ = "follow"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)
    target_id = Column(ForeignKey("user.id", ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False, index=True)

    target = relationship("User", primaryjoin="Follow.target_id == User.id")
    user = relationship("User", primaryjoin="Follow.user_id == User.id")
