from fastapi import APIRouter
from .sendmail import router as signup_router

account_router = APIRouter()
account_router.include_router(signup_router)