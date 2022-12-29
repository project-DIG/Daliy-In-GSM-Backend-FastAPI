from fastapi import APIRouter, status, HTTPException, Depends
from core.config import settings
from db.session import get_db, get_redis_db
from models.Video import Video
from models.User import User
from schemas.signup import SignUp
from redis import StrictRedis
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{user_name}/video")
def user_video(user_name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == user_name).one_or_none()

    videos = db.query(Video).filter(Video.uploader_id == user.id).all()

    data = {
        "videos": [
            {
                "id": i.id,
                "title": i.title,
                "video_url": i.video_url,
                "like": i.like,
                "dislike": i.dislike,
                "tag": i.tag,
                "uploader_id": i.uploader_id,
            }
            for i in videos
        ]
    }
    return data
