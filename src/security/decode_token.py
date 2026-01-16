from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('JWT_SECRET_KEY')

def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, "HS256")
        return decoded_token
    except Exception as err:
        print("Error:", err)

