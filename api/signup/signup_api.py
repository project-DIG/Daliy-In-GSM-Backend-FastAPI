from fastapi import APIRouter
from .email import router as email_router
from .email_check import router as email_check_router
from .signup import router as signup_router

router = APIRouter()
router.include_router(email_router)
router.include_router(email_check_router)
router.include_router(signup_router)
