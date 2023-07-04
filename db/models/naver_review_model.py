from sqlalchemy import Column,Integer,String,DateTime,select,ForeignKey
from sqlalchemy.orm import relationship,selectinload,joinedload
from pydantic import BaseModel
from db.session import Base,session

class NaverReview(Base):
    __tablename__ = 'naver_review'
    
    idx = Column(Integer,primary_key=True,nullable=False)
    original_review_id = Column(Integer,nullable=False)
    review_type = Column(String(20),nullable=False,default='NO_TYPE')
    review_content_type = Column(String(30),nullable=False,default='NO_CONTENT_TYPE')
    review_score = Column(nullable=False,default='0.0')
    review_content = Column(String,nullable=False)
    original_create_datetime = Column(DateTime)
    original_product_no = Column(Integer,nullable=False)
    original_product_url = Column(String)
    attach_url = Column(String, nullable=True, default=None)
    write_member_id = Column(String)
    insert_datetime = Column(DateTime)

# class TestTable(Base):
#     __tablename__ = 'test'
#     id = Column(Integer,primary_key=True,index=True)
#     title = Column(String(20),nullable=False)
#     description = Column(String)
    
class NR(BaseModel):
    idx : int
    original_review_id : int
    review_type : str
    review_content_type : str
    review_score : float
    review_content : str
    original_product_no : int
    original_product_url : str
    attach_url : str
    write_member_id : str