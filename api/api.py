from fastapi import APIRouter
from .signup.signup_api import router as signup_router
from .signin.signin_api import router as signin_router

api_router = APIRouter()
api_router.include_router(signup_router, prefix="/signup")
api_router.include_router(signin_router, prefix="/signin")
