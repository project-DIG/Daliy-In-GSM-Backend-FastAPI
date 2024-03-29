from fastapi import APIRouter
from .userpage import router as userpage_router
from .user_video import router as user_video_router
from .like_video import router as like_video_router
from .dislike_video import router as dislike_video_router
from .follow import router as follow_router
from .unfollow import router as unfollow_router
from .mini import router as mini_router

router = APIRouter()
router.include_router(mini_router)
router.include_router(userpage_router)
router.include_router(user_video_router)
router.include_router(like_video_router)
router.include_router(dislike_video_router)
router.include_router(follow_router)
router.include_router(unfollow_router)
