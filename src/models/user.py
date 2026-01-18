import datetime

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from ..models.thread import Thread
from .base import Base

class User(Base):
    __tablename__="user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    creation_date: Mapped[datetime.datetime] = mapped_column(nullable=False)

    threads: Mapped[list["Thread"]] = relationship(back_populates="user")

    def __repr__(self):
        return (
            f"<User "
            f"id={self.id} "
            f"email='{self.email}' "
            f"username='{self.username}' "
            f"password='{self.password}' "
            f"created={self.creation_date}>"
        )
