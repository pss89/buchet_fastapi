from datetime import datetime

from backend.domain.question.question_schema import QuestionCreate, QuestionUpdate
from backend.models import Question, User
from sqlalchemy.orm import Session


def get_question_list(db: Session, skip: int = 0, limit: int = 10):
    _question_list = db.query(Question)\
        .order_by(Question.create_date.desc())
        # .order_by(Question.create_date.desc())\
        # .all()
        
    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()
    
    # return question_list
    return total, question_list

"""
질문자에 대한 정보를 가져온다.
"""
def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(subject=question_create.subject,
                            content=question_create.content,
                            create_date=datetime.now())
    db.add(db_question)
    db.commit()
    
def create_quick_question(db: Session):
    for i in range(300):
        q = Question(subject='테스트 데이터입니다:[%03d]' % i,
                    content='내용 무', create_date=datetime.now())
        db.add(q)
        db.commit()
        
def update_question(db: Session, db_question: Question,
                    question_update: QuestionUpdate):
    db_question.subject = question_update.subject
    db_question.content = question_update.content
    db_question.modify_date = datetime.now()
    db.add(db_question)
    db.commit()
    
def delete_question(db: Session, db_question: Question):
    db.delete(db_question)
    db.commit()
    
def vote_question(db: Session, db_question: Question, db_user: User):
    db_question.voter.append(db_user)
    db.commit();