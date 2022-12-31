from fastapi import APIRouter, BackgroundTasks, HTTPException, status, Depends
from core.config import settings
from db.session import get_db, get_redis_db
from models.User import User
from schemas.signup import SendMail
from email.mime.text import MIMEText
from redis import StrictRedis
from sqlalchemy.orm import Session
import smtplib
import random
import string
import re


def send_mail(email: str, code: str):
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login("juwoon7163@gmail.com", "qghsykvilnjetxyz")
    with open("email_template/template.html", "r") as f:
        content = f.read().replace("{code}", code)
    msg = MIMEText(content, "html")
    msg["Subject"] = "Daily In GSM 인증메일"
    smtp.sendmail("juwoon7163@gmail.com", email, msg.as_string())
    smtp.quit()


router = APIRouter()


@router.post("/email")
def email(
    req: SendMail,
    background_tasks: BackgroundTasks,
    redis_db: StrictRedis = Depends(get_redis_db),
    db: Session = Depends(get_db),
):
    code = "".join([random.choice(string.digits) for i in range(6)])

    redis_db.delete("s210013@gsm.hs.kr")

    try:
        if req.email[0] != "s" or req.email[1:6].isdigit() == False:
            raise HTTPException(status.HTTP_410_GONE, detail="GSM 계정이 아닙니다.")
    except:
        raise HTTPException(status.HTTP_410_GONE, detail="GSM 계정이 아닙니다.")
    if redis_db.get(req.email) != None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="진행중인 인증이 있습니다.")
    elif db.query(User).filter(User.email == req.email).one_or_none() != None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="이메일이 사용중입니다.")
    else:
        redis_db.set(req.email, code, ex=settings.EMAIL_AUTH_EXPIRE)

    background_tasks.add_task(send_mail, req.email, code)
    return {"detail": "성공하였습니다."}
