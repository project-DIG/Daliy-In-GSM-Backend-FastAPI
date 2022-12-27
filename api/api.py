from fastapi import APIRouter
from .signup.signup_api import router as signup_router
from .signin.signin_api import router as signin_router
from .user.user_api import router as user_router

api_router = APIRouter()
api_router.include_router(signup_router, prefix="/signup", tags=["Signup"])
api_router.include_router(signin_router, prefix="/signin", tags=["Signin"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
