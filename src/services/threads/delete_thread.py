from src.database.db import Session
from sqlalchemy import delete

from src.models import Thread


def delete_thread(thread_id, user_id: str):
    with Session() as session:
        try:
            session.execute(delete(Thread).where(Thread.thread_id == thread_id, Thread.user_id == user_id))
            session.commit()
        except Exception as err:
            session.rollback()
            print("Error while deleting thread:", err)
