import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    creation_date: Mapped[datetime.datetime] = mapped_column(nullable=False)

    def __repr__(self):
        return (
            f"<User "
            f"id={self.id} "
            f"email='{self.email}' "
            f"username='{self.username}'"
            f"password='{self.password}' "
            f"created={self.creation_date}>"
        )
