from abc import ABC
from typing import List

from app.bases.article import ArticleBase
from app.models.article import Article

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.article import ArticleDTO


class ArticleCrud(ArticleBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def write(self, request_article: ArticleDTO) -> str:
        article = Article(**request_article.dict())
        self.db.add(article)
        self.db.commit()
        return "success"

    def update_article(self, request_article: ArticleDTO) -> str:
        pass

    def delete_article(self, page: int) -> List[Article]:
        pass

    def find_all_articles(self, request_article: ArticleDTO) -> ArticleDTO:
        pass

    def find_articles_by_userid(self, request_article: ArticleDTO) -> str:
        pass

    def find_article_by_title(self, request_article: ArticleDTO) -> str:
        pass


