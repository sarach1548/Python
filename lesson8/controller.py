from fastapi import FastAPI, HTTPException

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from task import task_router
from user import user_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(task_router, prefix='/task')
app.include_router(user_router, prefix='/user')
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event('startup')
async def print_something():
    print("Hello!!!!")


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
