from fastapi import APIRouter
from .signup.account_api import signup_router

api_router = APIRouter()
api_router.include_router(signup_router, prefix="/signup")
