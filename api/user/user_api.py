from fastapi import APIRouter
from .userpage import router as userpage_router

router = APIRouter()
router.include_router(userpage_router)
