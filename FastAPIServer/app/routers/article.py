from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.repositories.article as dao
from app.database import get_db

from app.schemas.article import Article




article_router = APIRouter()


@article_router.post("/")
async  def write(item: Article, db: Session = Depends(get_db)):
    article_dict = item.dict()
    print((f"SignUp Inform : {article_dict}"))
    dao.write(item=item,db=db)
    return {"data":"sucess"}

@article_router.post("/{id}")
async def login(id:str,item:Article, db: Session = Depends(get_db)):
    dao.login(id, item, db)
    return {"data": "success"}

@article_router.put("/{id}")
async def update(id:str,item: Article, db: Session = Depends(get_db)):
    dao.update(id=id,item=item,db=db)
    return {"data":"sucess"}

@article_router.delete("/{id}")
async def delete(id:str,user: Article, db: Session = Depends(get_db)):
    dao.delte(id=id,item=user,db=db)
    return {"data":"sucess"}

## Q
@article_router.get("/{page}")
async def get_posts(page, db: Session = Depends(get_db)):
    ls = dao.find_articles(page,db)
    return {"data": ls}

@article_router.get("/email/{id}")
async def get_post(id : str,db: Session = Depends(get_db)):
    dao.find_article(id=id,db=db)
    return {"data": "sucess"}

@article_router.get("/job/{search}/{no}")
async def get_post_by_title(search: str, page: int, db: Session = Depends(get_db)):
    dao.find_article_by_title(search,page,db)
    return {"data":"sucess"}
