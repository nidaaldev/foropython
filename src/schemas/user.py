from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    email: EmailStr
    password: str

class UserRegister(BaseUser):
    username: str
