from datetime import datetime

from backend.domain.question.question_schema import QuestionCreate, QuestionUpdate
from sqlalchemy import and_
from backend.models import Question, User, Answer
from sqlalchemy.orm import Session


def get_question_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = ''):
    # _question_list = db.query(Question)\
    #     .order_by(Question.create_date.desc())
    #     # .order_by(Question.create_date.desc())\
    #     # .all()
        
    # total = _question_list.count()
    # question_list = _question_list.offset(skip).limit(limit).all()
    
    question_list = db.query(Question)
    if keyword:
        search = '%%{}%%'.format(keyword)
        sub_query = db.query(Answer.question_id, Answer.content, User.username) \
            .outerjoin(User, and_(Answer.user_id == User.id)).subquery()
        question_list = question_list \
            .outerjoin(User) \
            .outerjoin(sub_query, and_(sub_query.c.question_id == Question.id)) \
            .filter(Question.subject.ilike(search) |        # 질문제목
                    Question.content.ilike(search) |        # 질문내용
                    User.username.ilike(search) |           # 질문작성자
                    sub_query.c.content.ilike(search) |     # 답변내용
                    sub_query.c.username.ilike(search)      # 답변작성자
                    )
    total = question_list.distinct().count()
    question_list = question_list.order_by(Question.create_date.desc())\
        .offset(skip).limit(limit).distinct().all()
        
    # return question_list
    return total, question_list

"""
질문자에 대한 정보를 가져온다.
"""
def get_question(db: Session, question_id: int, page: int = 0, size: int = 10):
    question = db.query(Question).get(question_id)
    
    # 페이징을 적용하여 answers를 가져옵니다.
    # total_answers = len(question.answers)
    # start = page * size
    #end = start + size
    #paginated_answers = question.answers[start:end]

    # Question 객체에 페이징된 answers를 설정합니다.
    #question.answers = paginated_answers
    #question.total_answers = total_answers  # 총 답변 수를 추가로 반환할 수 있습니다.
    
    return question

def create_question(db: Session, question_create: QuestionCreate, user: User):
    db_question = Question(subject=question_create.subject,
                            content=question_create.content,
                            create_date=datetime.now(),
                            user=user)
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
    
def update_views(db: Session, question_id: int):
    question = db.query(Question).filter(Question.id == question_id).first()
    if question:
        if question.views is None:
            question.views = 0
        question.views += 1
        db.commit()