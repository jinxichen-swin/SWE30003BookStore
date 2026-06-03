from database.connection import Base, engine
from database.models.feedback import Feedback  
from managers.feedback_manager import FeedbackManager

Base.metadata.create_all(engine)

manager = FeedbackManager(engine)

# feedback = manager.create_feedback(
#     user_id=1,
#     book_isbn=12,
#     rating=5,
#     comment="Great book!"
# )
# print("Created:", feedback.id)

# feedback = manager.create_feedback(
#     user_id=1,
#     book_isbn=2,
#     rating=1,
#     comment="shitty book.."
# )
# print("Created:", feedback.id)



all_feedbacks = manager.get_all_feedbacks()
for f in all_feedbacks:
    print(f"id={f.id}, user_id={f.user_id}, book_isbn={f.book_isbn}, rating={f.rating}, comment={f.comment}")


all_feedbacks = manager.get_feedback_by_user(1)
for f in all_feedbacks:
    print(f"id={f.id}, user_id={f.user_id}, book_isbn={f.book_isbn}, rating={f.rating}, comment={f.comment}")


