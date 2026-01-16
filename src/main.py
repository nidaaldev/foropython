from fastapi import FastAPI
from src.models.user import Base
from src.database.db import engine
from src.routes.users import router as users_router

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(users_router)
