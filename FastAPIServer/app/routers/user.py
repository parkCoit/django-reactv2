from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, paginate, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

from app.cruds.user import UserCrud
from app.admin.security import get_hashed_password, generate_token
from app.admin.utils import current_time
from app.database import get_db
from app.schemas.user import UserDTO, UserUpdate, UserList

user_router = APIRouter()


@user_router.post("/register", status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).add_user(request_user=dto)))


@user_router.post("/login", status_code=200)
async def login_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).login_user(request_user=dto)))


@user_router.post("/logout", status_code=200)
async def logout_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).logout_user(request_user=dto)))


@user_router.post("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=jsonable_encoder(
                                UserCrud(db).find_user_by_token(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@user_router.put("/modify")
async def modify_user(dto : UserDTO, update: UserUpdate, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).update_user(update)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@user_router.put("/reset-password")
async def reset_password(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).reset_password(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@user_router.delete("/delete", tags=['age'])
async def remove_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).delete_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@user_router.get("/page/{page}", response_model=Page[UserList])
async def get_users_per_page(page: int, db: Session = Depends(get_db)):
    results = UserCrud(db).find_all_users_order_by_created()
    default_size = 5
    page_result = paginate(results, Params(page=page, size=default_size))
    count = UserCrud(db).count_all_users()
    dc = {"count": count, "pager": page_result}
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(dc))


@user_router.get("/page/{page}/size/{size}", response_model=Page[UserList])
async def get_users_changed_size(page: int, size:int, db: Session = Depends(get_db)):
    results = UserCrud(db).find_all_users_order_by_created()
    page_result = paginate(results, Params(page=page, size=size))
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(page_result))


@user_router.get("/job/{search}/{page}")
async def get_users_by_job(search:str, page: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(
                            UserCrud(db).find_users_by_job(search, page,db)))