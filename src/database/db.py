from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///src/database.db", echo=True, connect_args={"check_same_thread": False})

Session = sessionmaker(bind=engine)
