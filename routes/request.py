from fastapi import APIRouter
from typing import List,Optional
from db.session import session
from db.models.naver_review_model import NaverReview,NR

import requests,json
from datetime import datetime
# from sqlalchemy

router = APIRouter(
    prefix='/request'
)

# naver review parsing
@router.get("")
def naver_review_parsing(merchantNo:str, originalProductNo:str, page:int):
    
    # uri 에 있는 번호는 상품테이블의 index인듯 ex)6076779843
    # merchantNo 500070063 판매자센터 번호
    # originProductNo 4923743074 상품번호
    # page 1
    # pageSize 20 (최대 30까지 가능)
    # user
    url = "https://brand.naver.com/n/v1/reviews/paged-reviews"
    data = {
        "merchantNo":merchantNo,
        "originProductNo":originalProductNo,
        "page":page,
        "pageSize":"20"
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }
    
    request = requests.post(url,json=data,headers=headers)
    
    # true 면 진행
    response_check = request.ok
    
    response = {}
    if response_check==True:
        response_data = request.json()

        json_load = json.dumps(response_data)
    
        data_list = json.loads(json_load)
        
        for key, value in data_list.items():
            if key == 'contents':
                for item in value:
                    time_str = item['createDate']
                    datetime_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%f%z")
                    formatted_time_str = datetime_obj.strftime("%Y%m%d%H%M%S")

                    review_attaches = json.dumps(item['reviewAttaches']) if len(item['reviewAttaches']) > 0 else None

                    nr = NaverReview()

                    nr.merchant_no = merchantNo
                    nr.original_review_id = item['id']
                    nr.review_type = item['reviewType']
                    nr.review_content_type = item['reviewContentClassType']
                    nr.review_score = item['reviewScore']
                    nr.review_content = item['reviewContent']
                    nr.original_create_datetime = formatted_time_str
                    nr.original_product_no = item['productNo']
                    nr.original_product_url = item['productUrl']
                    nr.attach_url = review_attaches
                    nr.write_member_id = item['writerMemberId']

                    session.add(nr)
                    session.commit()
                    
                    response['response_data'] = True
                    
    return response

@router.get("/oas_login")
def oa_request(user_id:str, password:str):
    url = "https://store.oa-world.com/login/login_request"
    data = {
        "email":user_id,
        "password":password
    }
    headers = {
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }
    
    
    request = requests.post(url,data=data,headers=headers)
    
    print(request.headers)
    # print(request.text)
    # print(request.content)
    # print(request.json())
    
    pass