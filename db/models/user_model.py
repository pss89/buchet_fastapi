from sqlalchemy import Column,Integer,String,DateTime,select,ForeignKey
from sqlalchemy.orm import relationship,selectinload,joinedload
from pydantic import BaseModel
from db.session import Base,session
from typing import List,Optional

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
    
    # user_info_detail에 foreignkey 가 있는것을 확인한다
    details = relationship("UserInfoDetail")
        
    # user_info, user_info_detail 테이블 join 한 쿼리 호출하기 위한 함수
    def get_users(userId: Optional[str] = None):
        # users = session.query(UserInfo).join(UserInfo.details).all()
        # users = (
        #     session.query(UserInfo)
        #     .join(UserInfo.details)
        #     .options(selectinload(UserInfo.details))
        #     .filter(UserInfo.user_id == userId)
        #     # .filter(UserInfo.user_id == user_id)
        #     .all()
        # )

        query = session.query(UserInfo).join(UserInfo.details).options(selectinload(UserInfo.details))

        if userId is not None:
            query = query.filter(UserInfo.user_id == userId)

        users = query.all()
        # return users
        
        return users
class UserInfoDetail(Base):
    __tablename__ = 'user_info_detail'
    # foreignkey 를 정의해줘야 join 가능
    user_id = Column(String(50),ForeignKey("user_info.user_id"),primary_key=True,nullable=False)
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