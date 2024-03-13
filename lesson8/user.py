import uvicorn
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from fastapi.middleware.cors import CORSMiddleware

user_router = APIRouter()


class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    taskId: int

    @field_validator('taskId')
    def check_user(cls, userId):
        if userId < 0:
            raise ValueError('error')
        return userId


users = {}


async def getId(id: int):
    if users[id] is not None:
        return False
    return True


@user_router.get("/")
async def getUsers():
    return users
    # raise HTTPException(status_code=404, detail="oops... your task didn't find")


@user_router.post("/")
async def add_task(user: User, is_exist: bool = Depends(getId)):
    try:
        if is_exist:
            users[user.userId] = user
        else:
            raise HTTPException(status_code=422, detail="Id user exist!")
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"


@user_router.put("/{id}", response_model=User)
async def update_task(id: int, item: User):
    update_item = jsonable_encoder(item)
    users[id] = update_item
    return update_item


@user_router.delete("/{id}")
async def delete_task(id: int):
    del users[id]
    return {"message": "Item deleted"}
