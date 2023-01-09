from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Session, relationship, declarative_base

Base = declarative_base()
class Post(Base):
    __tablename__ = 'posts'
    use_in_migration = True
    post_id = Column(primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(100))
    create_at = Column(DateTime)
    updated_at = Column(DateTime)

    class Config:
        arbitrary_types_allowed = True
