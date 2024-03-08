# main.py

from fastapi import FastAPI
from typing import List,Optional
from starlette.middleware.cors import CORSMiddleware
# from backend.routes.test import router as test
# from backend.routes.users import router as user
# from backend.routes.request import router as request
# from backend.routes.jwt import router as jwt

from backend.domain.answer import answer_router
from backend.domain.question import question_router
from backend.domain.user import user_router

import fastapi

app = FastAPI() # FastAPI 모듈

origins = [
    "http://localhost:5173" # frontend svelte에서 호출하는 origin 주소
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework-FastAPI "+fastapi.__version__
    }
    
@app.get("/hello")
def hello():
    return {"message": "Hello, Python & Svelte"}

app.include_router(answer_router.router)
app.include_router(question_router.router)
app.include_router(user_router.router)

# routes 폴더에 추가 된 route 파일들 호출
# app.include_router(test)
# app.include_router(request)
# app.include_router(user)
# app.include_router(jwt)

# 앞으로 할 것
# fastapi 로 아래 항목들 설치 및 사용하는 방법 알려줘

# - 이메일 전송
# - 슬랙 전송
# - 카카오 & 네이버 소셜 로그인
# - 레디스 사용