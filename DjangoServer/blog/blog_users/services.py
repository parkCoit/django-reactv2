import pandas as pd
from random_id import random_id
from sqlalchemy import create_engine

class UserServices(object):
    def __init__(self):
        global  random, random_email, random_nickname, random_password, engine
        # random = [random_id() for i in range(100)]
        random_email = [f'{random_id()}@naver.com' for i in range(100)]
        random_nickname = [random_id() for i in range(100)]
        random_password = [random_id() for i in range(100)]
        engine = create_engine(
             "mysql+pymysql://root:root@localhost:3306/mydb",
             encoding='utf-8')

    def insert_users(self):
        dc = self.create_user()
        ls = self.create_users(dc)
        df = self.change_to_df_users(ls)
        df.to_sql(name='blog_users',
                   if_exists='append',
                   con=engine,
                   index=False)

    def create_user(self):
        pass


    def get_user(self):
        df = pd.DataFrame({
            # 'blog_userid' : random,
            'email' : random_email,
            'nickname' : random_nickname,
            'password' : random_password
        })
        ls = list(df)
        # df.duplicated(['blog_userid'])
        return ls


if __name__ == '__main__':
    UserServices().get_user()