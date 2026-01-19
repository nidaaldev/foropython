from sqlalchemy import insert

from src.database.db import Session
from src.models import Thread


async def create_thread(user, thread):
    with Session() as session:
        try:
            session.execute(insert(Thread).values(
                title=thread.title,
                content=thread.content,
                user_id=user.id,
            ))

            session.commit()

            print("Post created!")

            return thread.title, thread.content

        except Exception as err:
            raise Exception("Error while creating a post:", err)
