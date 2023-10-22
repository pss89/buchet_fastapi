from fastapi import APIRouter, Form, HTTPException
from typing import List,Optional
from backend.db.session import session
from backend.db.models.naver_review_model import NaverReview,NR

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email_validator import validate_email

import requests,json
from datetime import datetime
# from sqlalchemy

router = APIRouter(
    prefix='/request'
)

@router.get("/hello")
def hello():
    return {"message": "안녕하세요 파이보"}

# @app.post("/send-email")
@router.get("send-email")
async def send_email(
    # to_email: str = Form(...),
    # subject: str = Form(...),
    # message: str = Form(...)
):
    gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
    gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
    
    # 로그인
    my_account = ""
    my_password = ""
    smtp.login(my_account, my_password)
    
    # 메일을 받을 계정
    to_mail = "sosn3@naver.com"
    
    # 메일 기본 정보 설정
    msg = MIMEMultipart()
    msg["Subject"] = f"첨부 파일 확인 바랍니다"  # 메일 제목
    msg["From"] = my_account
    msg["To"] = to_mail
    
    # 메일 본문 내용
    content = "안녕하세요. \n\n\
    데이터를 전달드립니다.\n\n\
    감사합니다\n\n\
    "
    content_part = MIMEText(content, "plain")
    msg.attach(content_part)
    
    # 이미지 파일 추가
    # image_name = "test.png"
    # with open(image_name, 'rb') as file:
    #     img = MIMEImage(file.read())
    #     img.add_header('Content-Disposition', 'attachment', filename=image_name)
    #     msg.attach(img)
    
    # 받는 메일 유효성 검사 거친 후 메일 전송
    # sendEmail(to_mail)
    smtp.sendmail(my_account, to_mail, msg.as_string())

    # 이메일 주소 유효성 검사
    # try:
    #     valid = validate_email(to_email)
    #     to_email = valid.email
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail="Invalid email address")

    # # 이메일 서버 설정
    # smtp_server = "smtp.gmail.com"
    # smtp_port = 465
    # smtp_username = "buchettest89@gmail.com"
    # smtp_password = "qkr@20080521"

    # # 이메일 내용 생성
    # msg = MIMEMultipart()
    # msg["From"] = formataddr((str(Header("Your Name", "utf-8")), "seongsigbag2@gmail.com"))
    # # msg["To"] = to_email
    # # msg["Subject"] = subject
    # # msg.attach(MIMEText(message, "plain"))
    # msg["To"] = 'sosn3@naver.com'
    # msg["Subject"] = 'fastapi 에서 보냄'
    # msg.attach(MIMEText('테스트 이메일 발송', "plain"))

    # try:
    #     # 이메일 전송
    #     with smtplib.SMTP(smtp_server, smtp_port) as server:
    #         server.starttls()
    #         server.login(smtp_username, smtp_password)
    #         server.sendmail(smtp_username, to_email, msg.as_string())
    #     return {"message": "Email sent successfully"}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail="Failed to send email")
    
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

    loginCookie = request.cookies
    
    # print(loginCookie.get("OSSI"))
    
    headers['Cookie'] = "OSSI="+loginCookie.get("OSSI")

    # print(headers)
    # return False
    
    url = "https://store.oa-world.com/mypage/user_info"
    request = requests.post(url,data=data,headers=headers)
    # print(request.status_code)
    # print('------------')
    
    # print(request.url)
    # print('------------')
    
    # print(request.headers)
    # print('------------')
    
    # print(request.cookies)
    # print('------------')
    
    print(request.text)
    print('------------')
    
    # response = request.json()
    
    # print(response)
    # print('------------')
    
    # print(request.json())
    # print('------------')
    
    # print(request.raise_for_status())
    # print('------------')

    # print(request.body)
    # print('------------')
    
    # print(request.client)
    # print('------------')
    
    # print(request.is_secure)
    # print('------------')
    # print('header')
    # print(request.headers)
    # print('cookies')
    # print(request.cookies)
    # print('content')
    # print(request.content)
    # print('history')
    # print(request.history)
    # print(request.text)
    # print(request.content)
    # print(request.json())
    
    pass