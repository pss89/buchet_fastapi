# import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# @contextlib.contextmanager
# with get_db() as db:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()