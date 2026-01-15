from src.database.db import Session
from src.schemas.user import BaseUser
from src.security.create_token import create_token
from src.security.password import verify_password
from sqlalchemy import select
from src.models.user import User


async def authenticate_user(user: BaseUser):
    # Check if password match
    with Session() as session:
        result = session.execute(select(User).where(User.email == user.email)).fetchone()
        print(result)

        if result is not None:
            if verify_password(user.password.encode('UTF-8'), result[0].password):
                return create_token({"email":f"{result[0].email}"})

        return False

