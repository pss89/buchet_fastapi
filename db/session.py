from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base # Base 생성
from core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    # encoding="utf-8",
    # echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,autoflush=False,bind=engine
    )
)
Base = declarative_base()
Base.qurey = session.query_property()
# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base = declarative_base()