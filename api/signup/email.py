from fastapi import APIRouter, BackgroundTasks, HTTPException, status
from schemas.account import SendMail
from email.mime.text import MIMEText
import smtplib
import random
import string
import redis


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
def email(req: SendMail, background_tasks: BackgroundTasks):
    code = "".join([random.choice(string.digits) for i in range(6)])

    with redis.StrictRedis(host="127.0.0.1", port=6379, db=0) as conn:
        if conn.get(req.email) != None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="진행중인 인증이 있습니다.")
        conn.set(req.email, code, ex=10)

    background_tasks.add_task(send_mail, req.email, code)
    return {"message": "success"}
