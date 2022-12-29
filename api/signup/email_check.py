from fastapi import APIRouter, HTTPException, status, Depends
from core.config import settings
from db.session import get_redis_db
from schemas.signup import CheckCode
from redis import StrictRedis

router = APIRouter()


@router.post("/email/check")
def email_check(req: CheckCode, redis_db: StrictRedis = Depends(get_redis_db)):
    if redis_db.get(req.email) == None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="이 이메일로 진행중인 인증이 없습니다.")
    if redis_db.get(req.email).decode() == req.code:
        redis_db.set(req.email, "success", ex=settings.EMAIL_AUTH_EXPIRE)
        return {"detail": "성공하였습니다."}
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="인증번호가 다릅니다.")
