from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.database import get_db # db 연결 메서드
from backend.domain.answer import answer_schema, answer_crud # 답변자에 대한 db 스크마, crud 정보
from backend.domain.question import question_crud # 질문자에 대한 처리

# 라우터 기본정보
router = APIRouter(
    prefix="/api/answer",
)

# 답변 등록
@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: int,
                  _answer_create: answer_schema.AnswerCreate,
                  db: Session = Depends(get_db)):
    # 해당 질문내역이 있는지 체크
    question = question_crud.get_question(db, question_id=question_id)
    # create answer
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    answer_crud.create_answer(db, question=question,
                              answer_create=_answer_create)
