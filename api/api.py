from fastapi import APIRouter
from .account.api import account_router

api_router = APIRouter()
api_router.include_router(account_router)