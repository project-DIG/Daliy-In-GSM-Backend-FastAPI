from fastapi import APIRouter
from .signup.signup_api import router as signup_router

api_router = APIRouter()
api_router.include_router(signup_router, prefix="/signup")
