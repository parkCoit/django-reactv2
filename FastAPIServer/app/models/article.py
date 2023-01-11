
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import UUIDType
from ..database import Base

from app.models.mixins import TimestampMixin


class Article(Base, TimestampMixin):
    __tablename__ = 'articles'
    use_in_migration = True
    art_seq = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(String(100), nullable=False)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'), nullable=True)

    user = relationship('User', back_populates='articles')

    class Config:
        arbitrary_types_allowed = True
