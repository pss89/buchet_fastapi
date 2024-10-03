# main.py

# import : 모듈 전체 호출
# from : 모듈 내에서 특정 함수, 클래스 호출

from fastapi import FastAPI, __version__
from typing import List,Optional
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

# from backend.routes.test import router as test
# from backend.routes.users import router as user
# from backend.routes.request import router as request
# from backend.routes.jwt import router as jwt

from backend.domain.answer import answer_router
from backend.domain.question import question_router
from backend.domain.user import user_router

import logging
import subprocess

app = FastAPI() # FastAPI 모듈

# svelte frontend에서 호출하는 origin 주소
origins = [
    "http://localhost:3000" # frontend svelte에서 호출하는 origin 주소
]

# 미들웨어 체크
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# app에 include 할 router 정보
app.include_router(answer_router.router)
app.include_router(question_router.router)
app.include_router(user_router.router)
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))

# Route Path
@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")

@app.get("/hello")
def hello():
    front_foler = "frontend"
    
    # npm list svelte 명령을 실행하고 결과를 캡처합니다.
    result = subprocess.run(
        ["npm", "list", "svelte"], 
        capture_output=True, 
        text=True, 
        check=False,
        cwd=front_foler
    )
    
    # 결과에서 svelte 버전을 추출합니다.
    output = result.stdout

    # 'svelte@version' 형태의 문자열에서 버전만 추출
    version_lines = [line for line in output.splitlines() if "svelte@" in line and not "deduped" in line]
    svelte_version = version_lines[-1].split('@')[1].strip()
    
    return {
        "message": "Hello, Python & Svelte",
        "Python-Framework": "FastAPI "+__version__,
        "Svelte-Framework": "Svelte "+svelte_version
    }
    
@app.get("/todoList")
def todoList():
    return {
        "todoList": [
            {"id": 1, "title": "답변 페이징과 정렬"},
            {"id": 2, "title": "댓글"},
            {"id": 3, "title": "카테고리"},
            {"id": 4, "title": "비밀번호 찾기와 변경"},
            {"id": 5, "title": "프로필"},
            {"id": 6, "title": "최근 답변과 최근 댓글"},
            {"id": 7, "title": "조회 수(완료)"},
            {"id": 8, "title": "소셜 로그인"},
            {"id": 9, "title": "마크다운 에디터"},
        ]
    }

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