from datetime import datetime

from sqlalchemy.orm import Session

from backend.domain.answer.answer_schema import AnswerCreate, AnswerUpdate
from backend.models import Question, Answer, User


def create_answer(db: Session, question: Question, answer_create: AnswerCreate, user: User):
    db_answer = Answer(question=question,
        content=answer_create.content,
        create_date=datetime.now(),
        user=user)
    db.add(db_answer)
    db.commit()

def get_answer(db: Session, answer_id: int):
    return db.query(Answer).get(answer_id)

def update_answer(db: Session, db_answer: Answer,
                    answer_update: AnswerUpdate):
    db_answer.content = answer_update.content
    db_answer.modify_date = datetime.now()
    db.add(db_answer)
    db.commit()
    
def delete_answer(db: Session, db_answer: Answer):
    db.delete(db_answer)
    db.commit()
    
def vote_answer(db: Session, db_answer: Answer, db_user: User):
    db_answer.voter.append(db_user)
    db.commit()
    
def create_quick_answer(db: Session, question: Question):
    for i in range(300):
        a = Answer(question=question,
                    content='테스트 데이터입니다:[%03d]' % i,
                    create_date=datetime.now(),
                    user_id=1)
        db.add(a)
        db.commit()