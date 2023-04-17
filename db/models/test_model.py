# models/test_model.py

# from sqlalchemy import Column, String, Integer, ForeignKey
# from sqlalchemy.orm import relationship
# from db.session import Base


# class Test(Base):
#     __tablename__ = "test"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)

from sqlalchemy import Column,Integer,String
from pydantic import BaseModel
from db.session import Base
# from db.session import engine

class TestTable(Base):
    __tablename__ = 'test'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(20),nullable=False)
    description = Column(String)
    
class Test(BaseModel):
    id : int
    title : str
    description : str