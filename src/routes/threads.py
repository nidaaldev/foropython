from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.responses import JSONResponse

from src.models import User
from src.schemas.thread import BaseThread as ThreadCreate
from src.security.dependencies import get_current_user
from src.services.threads.create_thread import create_thread
from src.services.threads.delete_thread import delete_thread as delete_thread_service

router = APIRouter()

@router.post("/create-thread")
async def post_thread(thread: ThreadCreate, user=Depends(get_current_user)):
    result = await create_thread(user, thread)

    return JSONResponse(
        status_code=201,
        content={
            "status": "success",
            "message": "Thread successfully created",
            "data": {
                "title": result[0],
                "content": result[1],
            },
        },
    )

@router.delete("/delete-thread/{thread_id}")
async def delete_thread(thread_id: int, user: User = Depends(get_current_user)):

    try:
        delete_thread_service(thread_id, user.id)

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": "Thread successfully deleted",
            },
        )

    except Exception as err:
        print("Error while deleting thread:", err)
        raise HTTPException(status_code=403, detail="Thread could not be deleted")
