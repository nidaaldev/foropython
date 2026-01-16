from datetime import datetime, timezone, timedelta
from jose import jwt

from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGHORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_token(data: dict, expire_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGHORITHM)

print(create_token({"user": "user1"}))
