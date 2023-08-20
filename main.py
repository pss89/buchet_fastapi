# main.py

from fastapi import FastAPI
from typing import List,Optional
from starlette.middleware.cors import CORSMiddleware
from routes.test import router as test
from routes.users import router as user
from routes.request import router as request
from routes.jwt import router as jwt
import fastapi

app = FastAPI() # FastAPI 모듈

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework-FastAPI "+fastapi.__version__
    }
    
# routes 폴더에 추가 된 route 파일들 호출
app.include_router(test)
app.include_router(user)
app.include_router(request)
app.include_router(jwt)

# 앞으로 할 것
# fastapi 로 아래 항목들 설치 및 사용하는 방법 알려줘

# - 이메일 전송
# - 슬랙 전송
# - 카카오 & 네이버 소셜 로그인
# - 레디스 사용