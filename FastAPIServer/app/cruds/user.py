from abc import ABC
from typing import List

from sqlalchemy import select

from app.admin.security import verify_password
from app.bases.user import UserBase
from app.database import conn
from app.models.user import User
from app.schemas.user import UserDTO
import pymysql
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        self.db.add(user)
        self.db.commit()
        return "success"

    def login(self, request_user: UserDTO) -> User:
        target = self.find_user_by_id(request_user)
        verified = verify_password(plain_password=request_user.password,
                                   hashed_password=target.password)
        print(f"로그인 검증 결과 : {verified}")
        if verified :
            return target
        else:
            return None

    def update_user(self, request_user: UserDTO) -> str:
        update_user = User(**request_user.dict())
        return update_user

    def delete_user(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        delete = self.db.query(User).filter(User.email == user.email).first()
        self.db.delete(delete)
        self.db.commit()
        return "success"

    def find_all_users(self, page: int) -> List[User]:
        print(f" page number is {page}")
        return self.db.query(User).all()

    def find_user_by_id(self, request_user: UserDTO) -> UserDTO:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.userid == user.userid).first()

    def find_userid_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.email == user.email).first()
        if db_user is not None:
            return db_user.userid
        else:
            return ""
