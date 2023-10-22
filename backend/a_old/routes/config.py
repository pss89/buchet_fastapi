import os
from dotenv import load_dotenv

from fastapi import APIRouter
from typing import List,Optional
from backend.db.session import session

class Setting:
    load_env = load_dotenv()
    router = APIRouter(
        # prefix="/items", # url 앞에 고정적으로 붙는 경로추가
    ) # Route 분리
    list = List
    db_session = session
    python_os = os