import uvicorn
from fastapi_pagination import add_pagination
from starlette.responses import HTMLResponse

from app.admin.utils import current_time
from app.database import init_db
from app.env_localhost import DB_URL
from app.routers.user import user_router
from app.routers.article import article_router
from app.test.user import test_router
from app.admin.pagenation import pagination_router
from mangum import Mangum

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
router.include_router(test_router, prefix="/test", tags=["test"])
router.include_router(pagination_router, prefix="/pagination", tags=["pagination"])

app = FastAPI()
add_pagination(app) # 페이지 설정
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
async def home():
    return HTMLResponse(content=f"""
    <body>
    <div style="width: 400px; margin: 50px auto;">
        <h1>현재 서버 구동 중 입니다.</h1>
        <h2>{current_time()}</h2>
    </div>
    </body>
    """)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/no-match-token")
async def no_match_token():
    return {"message" : f"토큰 유효시간이 지남"}


handler = Mangum(app)








