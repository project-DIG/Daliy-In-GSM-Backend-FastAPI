from fastapi import APIRouter, status, HTTPException, Depends
from core.config import settings
from db.session import get_db, get_redis_db
from models.Follow import Follow
from models.User import User
from utils.token import get_current_user
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{user_name}/unfollow")
def unfollow_user(user_name: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user_id = db.query(User).filter(User.email == current_user["email"]).one_or_none()
    target_id = db.query(User).filter(User.name == user_name).one_or_none()

    if target_id == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="유저가 존재하지 않습니다.")

    if user_id == target_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="자기자신은 언팔로우할 수 없습니다.")

    if db.query(Follow).filter((user_id == user_id) & (target_id == target_id)).one_or_none() == None:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="팔로우하지 않은 사용자입니다.")

    db.query(Follow).filter((user_id == user_id) & (target_id == target_id)).delete()

    return {"detail": "성공하였습니다."}
