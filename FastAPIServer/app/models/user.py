from uuid import uuid4

from ..database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Session, relationship, declarative_base
from sqlalchemy_utils import UUIDType


from app.models.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    user_id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    user_email = Column(String(20))
    password = Column(String(20), nullable=False)
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))

    articles = relationship('Article', back_populates='user')


    class Config:
        arbitrary_types_allowed = True
