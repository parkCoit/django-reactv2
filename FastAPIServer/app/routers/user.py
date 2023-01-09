from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.repositories.user as dao
from app.database import get_db


user_router = APIRouter()


@user_router.get('/', tags=["users"])
async def get_users(db : Session = Depends(get_db)):
    return {"data" : dao.find_users(db=db)}

post_router = APIRouter()

@post_router.get('/', tags=["posts"])
async def get_posts(db : Session = Depends(get_db)):
    return {"data" : dao.find_posts(db=db)}


