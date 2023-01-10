
from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware

from app.database import init_db
from app.env import DB_URL
from app.routers.user import user_router
from app.routers.article import article_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(article_router, prefix="/posts", tags=["posts"])

app = FastAPI()

app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)


@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": 'Welcome'}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}








