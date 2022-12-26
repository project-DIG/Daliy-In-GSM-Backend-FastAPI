from fastapi import Request, HTTPException, status
from core.config import settings
import datetime
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
    return jwt.decode(token, settings.JWT_SECRET, settings.JWT_ALGORITM)


def get_current_user(req: Request):
    if "Authorization" not in req.headers:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "토큰이 없습니다.")
    token = req.headers["Authorization"].split(" ")[1]

    return decode_token(token)
