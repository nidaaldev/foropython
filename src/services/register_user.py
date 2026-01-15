from datetime import datetime
from ..database.db import Session
from ..schemas.user import UserRegister as UserSchema
from ..models.user import User
from sqlalchemy import select, insert
from ..security.password import hash_password

async def register_user(user: UserSchema):
    with Session() as session:
        try:
            session.execute(insert(User)
            .values(
                email=user.email,
                username=user.username,
                password=hash_password(user.password.encode("utf-8")),
                creation_date=datetime.now()
            ))

            print("User registered:")
            result = session.execute(select(User).where(User.email == user.email)).fetchone()
            print(result)

            session.commit()
        except Exception as err:
                print(f"IntegrityError: {err}")
                raise Exception("Error while registering user:",err)

