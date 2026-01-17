from fastapi import APIRouter, HTTPException, Response, status, Depends
from ..schemas.user import UserRegister, BaseUser
from ..security.dependencies import get_current_user
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
async def login_user(response: Response, user: BaseUser):
        jwt = await authenticate_user(user)

        if not jwt:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        
        response.set_cookie(key="jwt", value=jwt, httponly=True)
        return {"message": "Login successful"}

@router.get("/dashboard")
def get_dashboard(current_user = Depends(get_current_user)):
     return current_user
