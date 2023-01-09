from sqlalchemy.orm import Session


from app.models.user import User, Post


def find_users(db: Session):
    return db.query(User).all()

def find_posts(db : Session):
    return db.query(Post).all()


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




