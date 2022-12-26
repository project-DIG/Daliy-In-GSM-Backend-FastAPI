from pydantic import BaseModel


class SignIn(BaseModel):
    email: str
    password: str


class Refresh(BaseModel):
    refresh_token: str
