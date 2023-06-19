from fastapi import APIRouter
from typing import List,Optional
from db.session import session
from db.models.naver_review_model import NaverReview,NR

import requests,json
from bs4 import BeautifulSoup

router = APIRouter(
    prefix='/request'
)

@router.get("")
# def read_users(user_id:str):
def read_users():
    
    # merchantNo 500070063
    # originProductNo 4923743074
    # page 1
    # pageSize 20 (최대 30까지 가능)
    # user
    url = "https://brand.naver.com/n/v1/reviews/paged-reviews"
    data = {
        "merchantNo":"500070063",
        "originProductNo":"4923743074",
        "page":"1",
        "pageSize":"20"
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }
    
    response = requests.post(url,json=data,headers=headers)
    # response = requests.get(url)
    
    # true 면 진행
    response_check = response.ok
    
    response_data = False
    if response_check==True:
        response_data = response.json()
    
    json_load = json.dumps(response_data)
    data_list = json.loads(json_load)
    
    for key, value in data_list.items():
        # print(f"{key}: {value}")
        if key == 'contents':
            for item in value:
                # print(item)
                # count = 1
                for k,v in item.items():
                    # count += 1
                    print(f"{k}: {v}")
    # data_list = list(data_list)
    # print(data_list)
    # print(response_data)
    
    # try:
    #     parsed_data = json.loads(response_data)
    #     print("Valid JSON")
    #     for key,value in parsed_data.items():
    #         print(f"{key}: {value}")
    # except json.JSONDecodeError:
    #     print("Invalid JSON")
    
    # 리스트 형태로 구하기
    # data_list = list(response_data)

    # 리스트 데이터 확인
    # print(data_list)

    # soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    
    # title = soup.find("h1").text
    # links = soup.find_all("a")
    
    # print("Title:",title)
    # print("Links:")
    # for link in links:
    #     print(link["href"])
        
    # users = session.query(UserInfo).all()
    # user = session.query(UserInfo).get(user_id)
    # print(user_id)
    # user = UserInfo(user_id=user_id)
    # UserInfo 클래스에 get_user 메서드 호출
    # users = UserInfo.get_users(user_id)
    # users = UserInfo.get_users()
    # print(users)
    pass
    # return response_data

# @router.get("/join")
# def user_join():
#     pass