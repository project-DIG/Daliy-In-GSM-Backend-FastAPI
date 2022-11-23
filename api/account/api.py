from fastapi import APIRouter
from .sendmail import router as signup_router

account_router = APIRouter(prefix="/account")
account_router.include_router(signup_router)