from fastapi import APIRouter, status, HTTPException, Depends
from core.config import settings
from db.session import get_db, get_redis_db
from models.User import User
from schemas.account import SignUp
from redis import StrictRedis
import bcrypt

router = APIRouter()


@router.post("/")
def signup(req: SignUp, db=Depends(get_db), redis_db: StrictRedis = Depends(get_redis_db)):
    if redis_db.get(req.email) == None or redis_db.get(req.email).decode() != "success":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="이메일 인증이 완료되지 않았습니다.")

    hashed_password = bcrypt.hashpw(req.password.encode(), settings.HASH_SALT.encode()).decode()
    db.add(User(id=None, name=req.name, password=hashed_password, email=req.email, profile_image="null"))
    return {"detail": "성공하였습니다"}
