from fastapi import APIRouter, status, HTTPException, Depends
from core.config import settings
from db.session import get_db, get_redis_db
from models.Follow import Follow
from models.User import User
from schemas.signup import SignUp
from utils.token import get_current_user
from redis import StrictRedis
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{user_name}")
def userpage(user_name: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user = db.query(User).filter(User.name == user_name).one_or_none()

    if user == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="유저가 존재하지 않습니다.")

    data = {"name": user.name, "profile_image": user.profile_image}

    follower = len(db.query(Follow).filter(Follow.target_id == user.id).all())
    follow = len(db.query(Follow).filter(Follow.user_id == user.id).all())

    data["follower"] = follower
    data["follow"] = follow

    if (
        current_user != None
        and db.query(User).filter((User.id == user.id) & (User.email == current_user["email"])).one_or_none() != None
    ):
        data["is_mine"] = True

    else:
        data["is_mine"] = False

    return data
