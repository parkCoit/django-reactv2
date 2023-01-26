from faker import Faker
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.admin.utils import between_random_date

from app.cruds.user import UserCrud
from app.database import get_db
from app.schemas.user import UserDTO

pagination_router = APIRouter()


@pagination_router.get("/page/{request_page}")
def pagination(request_page: int, db: Session = Depends(get_db)):
    row_cnt = UserCrud(db).count_all_users()
    page_size = 10
    response_page = request_page - 1  # 넘겨받은 page번호를 인덱스 값으로 전환
    t = row_cnt // page_size
    t2 = row_cnt % page_size
    page_cnt = t if (t2 == 0) else t + 1
    t3 = page_cnt // page_size
    block_size = 10
    t4 = page_cnt % block_size
    block_cnt = t3 if (t4 == 0) else t3 + 1
    start_row_per_page = page_size * (response_page)
    response_block = (response_page) // block_size
    end_row_per_page = start_row_per_page + (page_size - 1) if request_page != page_cnt else row_cnt - 1
    start_page_per_block = response_block * block_size
    end_page_per_block = start_page_per_block + (block_size -1 ) if response_block != (block_cnt - 1) else page_cnt

    # 확인해보자
    """
    row_cnt = UserCrud(db).count_all_users() - 1 # 총 row의 index 개수 1부터 시작
    row_size = 5  # 한 페이지당 row 의 개수
    page_cnt = row_cnt // row_size if (
                row_cnt % row_size == 0) else row_cnt // row_size + 1  # ex 3.7 페이지는 4페이지     # row_size에 따른

    page_now = 3  # 현재 페이지 숫자
    page_start = (page_now - 1) * row_size if (page_now - 1) * row_size < row_cnt else None # 해당 페이지의 row 데이터의 시작 값
    page_end_if = row_cnt if page_now == page_cnt else None
    page_end = page_end_if if page_now >= page_cnt else (page_now) * row_size -1  # 해당 페이지의 row 데이터의 마지막 값
    block_size = 10
    block_cnt = page_cnt // page_size if page_cnt % block_size else page_cnt // page_size + 1
    block_start = 
    print(f"page_start : {page_start}")
    print(f"page_end : {page_end}")
    print(f"총 페이지 개수 : {page_cnt}")
    print(f"count is {row_cnt}")
    return JSONResponse(status_code=200,
                        content=dict(msg=row_cnt))
    """

    print("### 테스트 ### ")
    print(f"start_row_per_page ={start_row_per_page}")
    print(f"end_row_per_page ={end_row_per_page}")
    print(f"start_page_per_block ={start_page_per_block}")
    print(f"end_page_per_block ={end_page_per_block}")

    '''
    row_cnt = 11, page_size = 5
    page  row_start row_end
    1 = 0 ~ 4
    2 = 5 ~ 9
    3 = 10
    
     | ### 테스트 ###
    api   | row_start =5
    api   | row_end =10 -> 9
    api   | page_start =0
    api   | page_end =2
    api   |  count is 11
    '''
    print(f" count is {row_cnt}")
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=row_cnt))




@pagination_router.get("/many")
def insert_many(db: Session = Depends(get_db)):
    faker = Faker('ko_KR')
    [UserCrud(db).add_user(
        UserDTO(email=faker.email(), password="11aa",
                username=faker.name(), birth=between_random_date(),
                address=faker.city()))
        for i in range(100)]
    """
    [print(UserFaker(
        email=faker.email(),
        password="11aa",
        username=faker.name(),
        birth=between_random_date(),
        address=faker.city())) for i in range(5)]
    """
    """

    ls = []

    objects = [
        User(name="u1"),
        User(name="u2"),
        User(name="u3")
    ]
    s.bulk_save_objects(objects)"""

