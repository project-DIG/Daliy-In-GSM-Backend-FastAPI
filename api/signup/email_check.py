from fastapi import APIRouter, HTTPException, status
from core.config import settings
from schemas.account import CheckCode
import redis

router = APIRouter()


@router.post("/email/check")
def email_check(req: CheckCode):
    with redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB) as conn:
        if conn.get(req.email) == None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="이 이메일로 진행중인 인증이 없습니다.")
        if conn.get(req.email).decode() == req.code:
            conn.delete(req.email)
            return {"detail": "성공하였습니다."}
        else:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="인증번호가 다릅니다.")
