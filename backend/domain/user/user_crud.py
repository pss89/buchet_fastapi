# php로 따지면 model 역활
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from backend.domain.user.user_schema import UserCreate
from backend.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_create: UserCreate):
    db_user = User(username=user_create.username, 
        password=pwd_context.hash(user_create.password),
        email=user_create.email)
    db.add(db_user)
    db.commit()
    
def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()
    
def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()