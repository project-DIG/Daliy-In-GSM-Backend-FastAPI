from fastapi import APIRouter, BackgroundTasks
from schemas.account import SignUp


def send_mail(email: str):
    pass


router = APIRouter()


@router.post()
def signup(req: SignUp, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_mail, req.email)
