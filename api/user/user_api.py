from fastapi import APIRouter
from .userpage import router as userpage_router
from .user_video import router as user_video_router

router = APIRouter()
router.include_router(userpage_router)
router.include_router(user_video_router)
