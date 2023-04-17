# main.py

import os
from typing import List,Optional
from fastapi import FastAPI
# from routes.test import router as test_router
# from pydantic import BaseModel

from db.session import session
from db.models.test_model import TestTable,Test

app = FastAPI() # FastAPI 모듈
# app.include_router(test_router) # 다른 route파일들을 불러와 포함시킴

@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework-FastAPI",
    }
    
@app.get("/tests") # Route Path
def read_tests():
    tests = session.query(TestTable).all()
    return tests

@app.get("/tests/{test_id}") # Route Path
def read_test(test_id:int):
    test = session.query(TestTable).filter(TestTable.id == test_id).first()
    return test

@app.post("/tests") # Route Path
def create_tests(title:str, description:str):
    test = TestTable()
    test.title = title
    test.description = description
    
    session.add(test)
    session.commit()
    
    return f"{title} created..."

@app.put("/tests") # Route Path
def update_tests(tests:List[Test]):
    
    for i in tests:
        test = session.query(TestTable).filter(TestTable.id == i.id).first()
        test.title = i.title
        test.description = i.description
        session.commit()
        
        # return f"{i.title} updated" 
    return f"{test[0].title} update..."

@app.delete("/tests") # Route Path
def delete_tests(test_id:int):
    test = session.query(TestTable).filter(TestTable.id == test_id).delete()
    session.commit()
    
    return read_tests