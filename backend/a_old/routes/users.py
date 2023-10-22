from fastapi import APIRouter
from typing import List,Optional
from backend.db.session import session
from backend.db.models.user_model import UserInfo,UserInfoDetail

router = APIRouter(
    prefix='/users'
)

@router.get("")
# def read_users(user_id:str):
def read_users():
    # users = session.query(UserInfo).all()
    # user = session.query(UserInfo).get(user_id)
    # print(user_id)
    # user = UserInfo(user_id=user_id)
    # UserInfo 클래스에 get_user 메서드 호출
    # users = UserInfo.get_users(user_id)
    users = UserInfo.get_users()
    # print(users)
    # pass
    return users

# @router.get("/join")
# def user_join():
#     pass