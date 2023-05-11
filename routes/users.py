from fastapi import APIRouter
from typing import List,Optional
from db.session import session
from db.models.user_model import UserInfo,UserInfoDetail