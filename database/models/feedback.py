from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from database.connection import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_isbn: Mapped[str] = mapped_column(ForeignKey("books.isbn"))
    #order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    comment: Mapped[str] = mapped_column()  
    rating: Mapped[int] = mapped_column() #1-5?