from fastapi import FastAPI
from src.models.base import Base
from src.database.db import engine
from src.routes.users import router as users_router
from src.models import *  # Import needed to load all SQLAlchemy models into Base.metadata

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(users_router)
