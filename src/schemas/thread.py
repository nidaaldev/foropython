from pydantic import BaseModel

class BaseThread(BaseModel):
    title: str
    content: str

class ThreadUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
