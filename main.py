# main.py

from fastapi import FastAPI
from typing import List,Optional
from starlette.middleware.cors import CORSMiddleware
from routes.test import router as test_router

app = FastAPI() # FastAPI 모듈
app.include_router(test_router) # 다른 route파일들을 불러와 포함시킴

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
        "Python": "Framework-FastAPI",
    }