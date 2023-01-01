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


@router.get("/")
def minipage(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user = db.query(User).filter(User.email == current_user["email"]).one_or_none()

    return {"name": user.name, "profile_image": user.profile_image}
