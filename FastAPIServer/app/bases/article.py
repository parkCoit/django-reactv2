from abc import abstractmethod, ABCMeta
from typing import List

from app.models.article import Article
from app.schemas.article import ArticleDTO


class ArticleBase(metaclass=ABCMeta):

    @abstractmethod
    def add_articles(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def find_articles(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def write(self, request_article: ArticleDTO) -> Article: pass

    @abstractmethod
    def login(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def update(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def delete(self, page: int) -> List[Article]: pass

    @abstractmethod
    def find_article(self, request_article: ArticleDTO) -> ArticleDTO: pass

    @abstractmethod
    def find_articles_by_job(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def find_article_by_title(self, request_article: ArticleDTO) -> str: pass