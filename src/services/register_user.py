from datetime import datetime

from ..database.db import Session
from ..schemas.user import User as UserSchema
from ..models.user import User
from sqlalchemy import select, insert

def register_user(user: UserSchema):
    with Session() as session:
        try:
            session.execute(insert(User)
            .values(
                email=user.email,
                username=user.username,
                password=user.password,
                creation_date=datetime.now()
            ))

            print("User registered:")
            print(session.execute(select(User).where(User.email == user.email)).fetchone())
            print("a")

            session.commit()
        except Exception as err:
                print("Error while regitering user:", err)
                raise Exception("Error while registering user") from err

