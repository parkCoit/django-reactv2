from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.cruds.article import ArticleCrud
from app.database import get_db

from app.schemas.article import ArticleDTO

article_router = APIRouter()


@article_router.post("")
async  def write(articledto: ArticleDTO, db: Session = Depends(get_db)):
    articleclud = ArticleCrud(db)
    result = articleclud.write(request_article=articledto)
    return result

@article_router.post("/{id}")
async def login(id:str,item:ArticleDTO, db: Session = Depends(get_db)):
    articleclud = ArticleCrud(db)
    articleclud.login(id, item, db)
    return {"data": "success"}

@article_router.put("/{id}")
async def update(id:str,item: ArticleDTO, db: Session = Depends(get_db)):
    articleclud = ArticleCrud(db)
    articleclud.update(id=id,item=item,db=db)
    return {"data":"sucess"}

@article_router.delete("/{id}")
async def delete(id:str,user: ArticleDTO, db: Session = Depends(get_db)):
    articleclud = ArticleCrud(db)
    articleclud.delte(id=id,item=user,db=db)
    return {"data":"sucess"}

## Q
@article_router.get("/{page}")
async def get_posts(page, db: Session = Depends(get_db)):
    articleclud = ArticleCrud(db)
    ls = articleclud.find_articles(page,db)
    return {"data": ls}

@article_router.get("/email/{id}")
async def get_post(id : str,db: Session = Depends(get_db)):
    articleclud = ArticleCrud(db)
    articleclud.find_article(id=id,db=db)
    return {"data": "sucess"}

@article_router.get("/job/{search}/{no}")
async def get_post_by_title(search: str, page: int, db: Session = Depends(get_db)):
    articleclud = ArticleCrud(db)
    articleclud.find_article_by_title(search,page,db)
    return {"data":"sucess"}
