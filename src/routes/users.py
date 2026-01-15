from fastapi import APIRouter, HTTPException, status
from ..schemas.user import UserRegister, BaseUser
from ..services.authentication import authenticate_user
from ..services.register_user import register_user

router = APIRouter()

@router.post("/register")
async def read_user(user: UserRegister):
    try:
        await register_user(user)
    except Exception as err:
        print("Error while registering user:", err)
        raise HTTPException(status_code=400, detail="User could not be registered")
    return {"message": "User registered successfully"}

@router.post("/login")
async def login_user(user: BaseUser):
        result = await authenticate_user(user)

        if not result:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        return result
