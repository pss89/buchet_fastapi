from fastapi import APIRouter
from typing import List,Optional
from db.session import session
from db.models.user_model import UserInfo,UserInfoDetail

router = APIRouter()

@router.get("/users")
# def read_users(user_id:str):
def read_users():
    # users = session.query(UserInfo).all()
    # user = session.query(UserInfo).get(user_id)
    # print(user_id)
    # user = UserInfo(user_id=user_id)
    users = UserInfo.get_users()
    # print(users)
    # pass
    return users