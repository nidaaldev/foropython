from fastapi import HTTPException, status, Cookie
from .decode_token import decode_token
from src.database.db import Session
from sqlalchemy import select
from src.models.user import User


def get_current_user(jwt = Cookie(None)):
    if jwt is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    payload = decode_token(jwt)

    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user_email = payload.get("email")

    with Session() as session:
        result = session.execute(select(User).where(User.email == user_email)).fetchone()
    return result[0]
