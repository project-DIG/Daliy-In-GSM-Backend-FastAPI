from fastapi import Request, HTTPException, status
from core.config import settings
import datetime
from jwt import ExpiredSignatureError, InvalidTokenError
import jwt


def generate_token(payload: dict, type: str):
    if type == "refresh":
        payload["type"] = "refresh"
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.REFRESH_EXPIRE)

    elif type == "access":
        payload["type"] = "access"
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.ACCESS_EXPIRE)

    else:
        raise Exception("Token type must be 'refresh' or 'access'")

    return jwt.encode(payload, settings.JWT_SECRET, settings.JWT_ALGORITM)


def decode_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, settings.JWT_ALGORITM)
    except ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="만료된 토큰입니다.")
    except InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="올바르지 않은 토큰입니다.")
    return payload


def get_current_user(req: Request):
    if "Authorization" not in req.headers:
        return None
    try:
        token = req.headers["Authorization"].split(" ")[1]
    except:
        token = req.headers["Authorization"]

    return decode_token(token)
