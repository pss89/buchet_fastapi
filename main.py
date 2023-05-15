# main.py

from fastapi import FastAPI
from typing import List,Optional
from starlette.middleware.cors import CORSMiddleware
from routes.test import router as test_route
from routes.users import router as user_route

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
        "Python": "Framework-FastAPI",
    }
    
app.include_router(test_route)
app.include_router(user_route)