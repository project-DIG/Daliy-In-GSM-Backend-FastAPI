from fastapi import APIRouter, status, HTTPException
from schemas.signin import Refresh
from utils.token import generate_token, decode_token
from jwt import DecodeError, ExpiredSignatureError

router = APIRouter()


@router.post("/refresh")
def refresh(req: Refresh):
    try:
        payload = decode_token(req.refresh_token)
        access_token = generate_token(payload=payload, type="access")
        return {"detail": "성공하였습니다.", "access_token": access_token}

    except DecodeError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="토큰이 올바르지 않습니다.")

    except ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="만료된 토큰입니다.")
