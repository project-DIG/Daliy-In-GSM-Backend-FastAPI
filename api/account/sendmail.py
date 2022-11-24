from fastapi import APIRouter, BackgroundTasks, status
from fastapi import HTTPException
from random import sample
from string import ascii_letters, digits
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.config import settings
from schemas.account import SendMail
import aioredis
import smtplib

def send_mail(email_addr: str, code: str):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('juwoon7163@gmail.com', 'vqeixipthwzjdejf')
    
    msg = MIMEMultipart('alternative')
    
    msg['Subject'] = "Haine 인증 메일"
    msg['From'] = "juwoon7163@gmail.com"
    msg['To'] = email_addr
    
    with open("./template/email_template.html", "r", encoding="UTF-8") as f:
        template = f.read()
        
    msg.attach(MIMEText(template.replace("url", f"http://localhost:8080/account/signup?code={code}"), 'html'))

    s.send_message(msg)
    s.quit()

router = APIRouter()


@router.post("/sendmail")
async def sendmail(req: SendMail, background_tasks: BackgroundTasks):
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}/{settings.REDIS_DATABASE}", decode_responses=True)
    
    await redis.flushall()
    if await redis.get(req.email) != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="진행중인 인증이 있습니다")
    
    code = ''.join(sample(ascii_letters+digits, 10))
    await redis.set(req.email, code, ex=600) #10분 만료
    await redis.set(code, req.email, ex=600)
    
    background_tasks.add_task(send_mail, req.email, code)
    
    return {"detail": "성공하였습니다"}