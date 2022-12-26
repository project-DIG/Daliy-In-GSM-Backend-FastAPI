from fastapi import APIRouter, status, HTTPException, Depends
from core.config import settings
from db.session import get_db, get_redis_db
from models.Like import Like
from models.Video import Video
from models.User import User
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/{user_id}/video/like")
def like_video(user_id: int, db: Session = Depends(get_db)):
    likes = db.query(Like.video_id).filter((Like.user_id == user_id) & (Like.type == "like")).all()
    data = {"videos": []}
    for i in likes:
        video = db.query(Video).filter(Video.id == i[0]).one()
        data["videos"].append(
            {
                "id": video.id,
                "title": video.title,
                "video_url": video.video_url,
                "like": video.like,
                "dislike": video.dislike,
                "tag": video.tag,
                "uploader_id": video.uploader_id,
            }
        )
    return data
