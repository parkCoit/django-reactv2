from sqlalchemy.orm import Session


from app.models.user import User

# users
def join(item: User, db: Session):
    return None

def login(id: str, item: User, db: Session):
    return None

def update(id, item, db):
    return None

def delete(id, item, db):
    return None


def find_users(page:int, db: Session):
    print(f" page number is {page}")
    return db.query(User).all()

def find_user(id, db):
    return None

def find_users_by_job(search, page, db):
    return None



# 강사님 코드
# from app.database import create_mysql_engine, conn
# from app.models.user import User
# from sqlalchemy.orm import sessionmaker
# def find_users_legacy():
#     cursor = conn.cursor()
#     sql = "select * from users"
#     cursor.execute(sql)
#     return cursor.fetchall()
#



