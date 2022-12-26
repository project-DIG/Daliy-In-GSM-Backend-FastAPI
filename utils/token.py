from core.config import settings
import jwt


def generate_token(payload: dict, type: str):
    if type == "access":
        payload["type"] = "access"
    if type == "refresh":
        payload["type"] = "refresh"
    else:
        raise "Token type must be 'refresh' or 'access'"
    return jwt.encode(payload, settings.JWT_SECRET, settings.JWT_ALGORITM)


def decode_token(token: str):
    return jwt.decode(token, settings.JWT_SECRET, settings.JWT_ALGORITM)
