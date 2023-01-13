from sqlalchemy import select

from app.database import conn
from app.models.user import User
from app.schemas.user import UserDTO
import pymysql
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()

def join(userDTO: UserDTO, db: Session)->str:
    user = User(**userDTO.dict())
    db.add(user)
    db.commit()
    return "success"

# 로그인 선생님 방식
# def login(userDTO: UserDTO, db: Session):
#     user = User(**userDTO.dict())
#     print(f" email {user.user_email}")
#     db_user = db.scalars(select(User).where(User.user_email == user.user_email)).first()
#
#     print(f" dbUser {db_user}")
#     if db_user is not None:
#         if db_user.password == user.password:
#             return db_user
#     else:
#         print("해당 이메일이 없습니다.")
#         return "failure"

# 로그인 민호 방식
def login(userDTO: UserDTO, db: Session):
    user = User(**userDTO.dict())
    email = db.query(User).filter(User.user_email == user.user_email , User.password == user.password).first()
    if email is not None:
            return email
    else: return '이상해'

def update(id, item, db):
    return None

def delete(id, item, db):
    return None


def find_users(page:int, db: Session):
    print(f" page number is {page}")
    return db.query(User).all()

def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()

def find_user(id, db):
    return None

def find_users_by_job(search, page, db):
    return None