from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Session, relationship, declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    user_email = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))

    class Config:
        arbitrary_types_allowed = True

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
