from src.database.db import Session
from sqlalchemy import update, select

from src.models import Thread


async def update_thread(thread_id: int, user_id: str, thread_data):
    with Session() as session:
        try:
            # Check if thread exists and belongs to the user
            stmt = select(Thread).where(Thread.thread_id == thread_id, Thread.user_id == user_id)
            thread = session.execute(stmt).scalar_one_or_none()

            if not thread:
                return None

            update_data = thread_data.model_dump(exclude_unset=True)
            if not update_data:
                return thread

            session.execute(
                update(Thread)
                .where(Thread.thread_id == thread_id)
                .values(**update_data)
            )
            session.commit()
            
            # Refresh to get updated data
            session.refresh(thread)
            return thread

        except Exception as err:
            session.rollback()
            raise Exception("Error while updating thread:", err)
