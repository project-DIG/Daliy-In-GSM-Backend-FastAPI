from fastapi import APIRouter, status, HTTPException, Depends
from core.config import settings
from db.session import get_db, get_redis_db
from models.Follow import Follow
from models.User import User
from schemas.signup import SignUp
from redis import StrictRedis
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{user_id}")
def userpage(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).one_or_none()

    if user == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="유저가 존재하지 않습니다.")

    data = {"name": user.name, "profile_image": user.profile_image}

    follower = len(db.query(Follow).filter(Follow.target_id == user_id).all())
    follow = len(db.query(Follow).filter(Follow.user_id == user_id).all())

    data["follower"] = follower
    data["follow"] = follow

    return data
