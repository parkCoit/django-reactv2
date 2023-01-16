

from app.admin.utils import current_time
from app.database import init_db
from app.env import DB_URL
from app.routers.user import user_router
from app.routers.article import article_router

from fastapi import FastAPI, APIRouter, HTTPException, Depends
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
API_TOKEN = "SECRET_API_TOKEN"
api_key_header = APIKeyHeader(name="token")
print(f" ############ app.main Started At {current_time()} ############")

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(article_router, prefix="/article", tags=["posts"])

app = FastAPI()
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.router.redirect_slashes = False


app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)


@app.get("/protected-router")
async def protected_route(token: str = Depends(api_key_header) ):
    if token != API_TOKEN:
        raise HTTPException(status_code=403)
    return {"잘못된" : "경로입니다"}

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": 'Welcome'}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}








