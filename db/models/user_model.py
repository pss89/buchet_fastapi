from sqlalchemy import Column,Integer,String,DateTime
from pydantic import BaseModel
from db.session import Base

class UserInfo(Base):
    __tablename__ = 'user_info'
    user_id = Column(String(50),primary_key=True,nullable=False)
    password = Column(String(255),nullable=False)
    identifier = Column(String(20),nullable=False)
    leave_type = Column(String(1),nullable=False,default='N')
    drop_type = Column(String(1),nullable=False,default='N')
    join_datetime = Column(DateTime,nullable=False)
    leave_datetime = Column(DateTime)
    drop_datetime = Column(DateTime)
    insert_datetime = Column(DateTime)
    update_datetime = Column(DateTime)
    
class UserInfoDetail(Base):
    __tablename__ = 'user_info_detail'
    user_id = Column(String(50),primary_key=True,nullable=False)
    name = Column(String(15),nullable=False)
    gender_type = Column(String(20))
    nickname = Column(String(15))
    birth_date = Column(DateTime)
    contact = Column(String(11),nullable=False)
    contact_cert_type = Column(String(1),nullable=False,default='N')
    portal_user_id = Column(String(50))
    service_code = Column(String(10),nullable=False,default='default')
    email_cert_type = Column(String(1),nullable=False,default='N')
    update_datetime = Column(DateTime)