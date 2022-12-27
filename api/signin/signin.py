from fastapi import APIRouter, status, HTTPException, Depends
from core.config import settings
from db.session import get_db
from models.User import User
from schemas.signin import SignIn
from utils.token import generate_token
from sqlalchemy.orm import Session
import bcrypt

router = APIRouter()


@router.post("/")
def signin(req: SignIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == req.email).one_or_none()

    if user == None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="등록된 이메일이 아닙니다.")

    if bcrypt.checkpw(req.password.encode(), user.password.encode()) == False:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="비밀번호가 올바르지 않습니다.")

    refresh_token = generate_token(payload={"iss": "DIG", "email": req.email}, type="refresh")
    access_token = generate_token(payload={"iss": "DIG", "email": req.email}, type="access")

    return {"detail": "성공하였습니다.", "refresh_token": refresh_token, "access_token": access_token}
