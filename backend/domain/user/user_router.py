from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.database import get_db
from backend.domain.user import user_crud, user_schema

router = APIRouter(
    prefix="/api/user",
)

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user == user_crud.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail="이미 존재하는 사용자입니다.")
    user_crud.create_user(db, user_create=_user_create)