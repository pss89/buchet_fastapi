import os
from dotenv import load_dotenv

from fastapi import APIRouter
from typing import List,Optional
from db.session import session
from db.models.test_model import TestTable,Test

from apis.slack_api import SlackAPI
from fastapi.encoders import jsonable_encoder
import json

load_dotenv()

router = APIRouter(
    # prefix="/items", # url 앞에 고정적으로 붙는 경로추가
) # Route 분리

slack_token = os.getenv("SLACK_TOKEN")
slack = SlackAPI(slack_token)
slack_channel_id = slack.get_channel_id('noti_msg')

@router.get("/tests") # Route Path
def read_tests():
    tests = session.query(TestTable).all()

    return tests    
    # 채널아이디 파싱
    # response_result = slack.post_message(slack_channel_id,'fastapi에서 보낸 메시지')

    # if response_result != True: 
    #     return 'slack_error'
    # else:
    #     return tests
        
@router.get("/tests/{test_id}") # Route Path
def read_test(test_id:int):
    test = session.query(TestTable).filter(TestTable.id == test_id).first()
    return test

@router.post("/tests") # Route Path
def create_tests(title:str, description:str):
    test = TestTable()
    test.title = title
    test.description = description
    
    session.add(test)
    session.commit()
    
    return f"{title} created..."

@router.put("/tests") # Route Path
def update_tests(tests:List[Test]):
    
    for i in tests:
        test = session.query(TestTable).filter(TestTable.id == i.id).first()
        test.title = i.title
        test.description = i.description
        session.commit()
        
        # return f"{i.title} updated" 
    return f"{test[0].title} update..."

@router.delete("/tests") # Route Path
def delete_tests(test_id:int):
    test = session.query(TestTable).filter(TestTable.id == test_id).delete()
    session.commit()
    
    return f"{test_id} delete.."