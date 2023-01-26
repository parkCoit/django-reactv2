import pymysql

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.env import HOSTNAME, PORT, USERNAME, PASSWORD, CHARSET, DATABASE, DB_URL


Base = declarative_base()
engine = create_engine(DB_URL, encoding=CHARSET, echo=True)
pymysql.install_as_MySQLdb()
conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)
SessionLocal = scoped_session(
    sessionmaker(autocommit = False, autoflush=False, bind=engine)
)
Base.query = SessionLocal.query_property()



async def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e


async def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db = SessionLocal()
        db.close()