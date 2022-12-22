from fastapi import APIRouter
from .email import router as email_router
from .email_check import router as email_check_router

signup_router = APIRouter()
signup_router.include_router(email_router)
signup_router.include_router(email_check_router)
