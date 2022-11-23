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

template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h2 style = "font-size:48px; text-align:center; margin-bottom:10px;">Haine</h2>
    <div style = "width:20%; height:90px; background-color:#F8F9FA; 
    border-style:solid; border-color:#EAEDEF; border-width:2px; text-align:center;
    margin-left:auto; margin-right:auto; padding:10px;">
            <p style = "font-size:14px;width:100%; text-align:left; color:gray;  ">안녕하세요. Haine 입니다. 이 아래의 버튼을 누르시면 회원가입이 완료됩니다.본인이 요청하지 않으셨다면 메일을 무시해주세요.<p>
    </div>
    <div style="text-align: center; margin-top: 15px;">
        <button type="button" style="width:50%; background-color:pink; height:50px; text-align: center; line-height:50px; border: none;">계속하기</button>
    </div>
    <div style = "text-align:center;">
        <p style = "margin-bottom:0; color: gray; font-size:16px; margin-bottom: 0px;">위 버튼을 클릭하시거나 다음 링크를 눌러주세요</p>
        <a style = "color:pink" href = "url">url</a>
        <p style = "font-size: 15px; color: gray; letter-spacing: 0.0px;">이 링크는 24시간동안 유효합니다.</p>
    </div>
</body>
</html>
"""

def send_mail(email_addr: str, code: str):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('juwoon7163@gmail.com', 'vqeixipthwzjdejf')
    
    msg = MIMEMultipart('alternative')
    
    msg['Subject'] = "Haine 인증 메일"
    msg['From'] = "juwoon7163@gmail.com"
    msg['To'] = email_addr
    
    msg.attach(MIMEText(template.replace("url", f"http://localhost:8080/account/signup?code={code}"), 'html'))
    
    s.send_message(msg)
    s.quit()

router = APIRouter()


@router.post("/sendmail")
async def sendmail(req: SendMail, background_tasks: BackgroundTasks):
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}/{settings.REDIS_DATABASE}", decode_responses=True)
    
    if await redis.get(req.email) != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="진행중인 인증이 있습니다")
    
    code = ''.join(sample(ascii_letters+digits, 10))
    await redis.set(req.email, code, ex=6) #10분 만료
    await redis.set(code, req.email, ex=6)
    
    background_tasks.add_task(send_mail, req.email, code)
    
    return {"detail": "성공하였습니다"}