from pydantic import BaseModel


class SendMail(BaseModel):
    email: str


class CheckCode(BaseModel):
    email: str
    code: str


class SignUp(BaseModel):
    name: str
    password: str
    email: str
