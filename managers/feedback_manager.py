from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import ForeignKey
from database.models.feedback import Feedback
from sqlalchemy import create_engine, Engine

class FeedbackManager ():
    def __init__(self, engine: Engine):
        self.engine = engine

    def create_feedback(self, user_id: int, book_isbn: int, rating: int, comment: str) -> Feedback:
        with Session(self.engine,expire_on_commit=False) as session: 
            feedback_item = Feedback(user_id=user_id, book_isbn=book_isbn, rating=rating, comment=comment)
            session.add(feedback_item)
            session.commit()
            return feedback_item


#Get feedback
    def get_feedback(self, feedback_id: int) -> Feedback:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(Feedback).filter(Feedback.id == feedback_id).first()

    def get_feedback_by_user(self, user_id: int) -> list[Feedback]:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(Feedback).filter(Feedback.user_id == user_id).all()
        
    def get_feedback_by_book(self, book_isbn: int) -> list[Feedback]:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(Feedback).filter(Feedback.book_isbn == book_isbn).all()



#Update
    def update_rating(self, feedback_id: int, rating: str) -> Feedback:
        with Session(self.engine,expire_on_commit=False) as session:
            feedback = session.query(Feedback).filter(Feedback.id == feedback_id).first()
            if feedback:
                feedback.rating = rating
                session.commit()
            return feedback
    def update_comment(self, feedback_id:int, comment:str) -> Feedback:
        with Session(self.engine,expire_on_commit=False) as session:
            feedback = session.query(Feedback).filter(Feedback.id==feedback_id).first()
            if feedback:
                feedback.comment = comment
                session.commit()

        

#Statistic

    def get_all_feedbacks(self) -> list[Feedback]:
        with Session(self.engine, expire_on_commit=False) as session:
            return session.query(Feedback).all()


#Delete
    def delete_feedback(self, feedback_id: int) -> None:
        with Session(self.engine,expire_on_commit=False) as session:
            feedback_item = session.query(Feedback).filter(Feedback.id == feedback_id).first()
            if feedback_item:
                session.delete(feedback_item)
                session.commit()
