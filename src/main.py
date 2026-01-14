from fastapi import FastAPI
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from src.models.user import User, Base

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"

user1 = User(email="user@email.com", username="user1", password="asfhafjlsasfjfas")

engine = create_engine("sqlite:///src/database.db", echo=True)

Base.metadata.create_all(engine)
with Session(engine) as session:
    session.add(user1)
    statement = select(User).where(User.email == "user@email.com")
    user = session.scalars(statement).first()
    print(user)
    session.commit()


