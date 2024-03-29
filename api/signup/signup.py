from fastapi import APIRouter, status, HTTPException, Depends
from core.config import settings
from db.session import get_db, get_redis_db
from models.User import User
from schemas.signup import SignUp
from redis import StrictRedis
from sqlalchemy.orm import Session
import bcrypt

router = APIRouter()


@router.post("/")
def signup(req: SignUp, db: Session = Depends(get_db), redis_db: StrictRedis = Depends(get_redis_db)):
    if redis_db.get(req.email) == None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="인증이 만료되었거나 없습니다.")

    if redis_db.get(req.email).decode() != "success":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="진행중인 인증이 있습니다.")

    if db.query(User).filter(User.name == req.name).one_or_none() != None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="중복된 이름입니다.")

    hashed_password = bcrypt.hashpw(req.password.encode(), bcrypt.gensalt()).decode()
    db.add(
        User(
            id=None,
            name=req.name,
            password=hashed_password,
            email=req.email,
            profile_image="https://cdn.icon-icons.com/icons2/2468/PNG/512/user_user_profile_user_icon_user_thump_icon_149321.png",
        )
    )
    redis_db.delete(req.email)

    return {"detail": "성공하였습니다."}
