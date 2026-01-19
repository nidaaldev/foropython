from pydantic import BaseModel

class BaseThread(BaseModel):
    title: str
    content: str
