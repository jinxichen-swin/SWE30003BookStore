from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from database.connection import Base

class Shipment(Base):
    __tablename__ = "shipments"

    id: Mapped[int] = mapped_column(primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    #book_isbn: Mapped[str] = mapped_column(ForeignKey("books.isbn"))

    address: Mapped[str] = mapped_column()
    
    status: Mapped[str] = mapped_column()  # like "pending", "shipped", "delivered"?
    tracking_number: Mapped[str] = mapped_column()
