
from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware

from app.env import DB_URL
from app.routers.user import user_router, post_router




router = APIRouter()
router.include_router(user_router, prefix="/users",tags=["users"])
app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(post_router, prefix="/posts", tags=["posts"])
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

@app.get("/")
async def root():
    return {"message": 'Welcome'}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}








