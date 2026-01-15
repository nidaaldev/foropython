from fastapi import APIRouter, HTTPException, status
from ..schemas.user import User
from ..services.register_user import register_user

router = APIRouter()

@router.post("/register")
async def read_user(user: User):
    try:
        await register_user(user)
    except Exception as err:
        print("Error while registering user:", err)
        raise HTTPException(status_code=400, detail="User could not be registered")
    return {"message": "User registered successfully"}

