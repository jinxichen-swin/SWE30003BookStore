from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import ForeignKey
from database.models.shipment import Shipment
from sqlalchemy import create_engine, Engine

class ShipmentManager():
    def __init__(self, engine: Engine):
        self.engine = engine

    def create_shipment(self, order_id: int, user_id: int, address: str, courier: str, tracking_number: str) -> Shipment:
        with Session(self.engine,expire_on_commit=False) as session: 
            shipment = Shipment(order_id=order_id, user_id=user_id, address=address, courier=courier, status="pending", tracking_number=tracking_number)
            session.add(shipment)
            session.commit()
            return shipment


#Get shipment
    def get_shipment(self, shipment_id: int) -> Shipment:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(Shipment).filter(Shipment.id == shipment_id).first()

    def get_shipment_by_order(self, order_id: int) -> Shipment:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(Shipment).filter(Shipment.order_id == order_id).first()

    def get_shipment_by_user(self, user_id: int) -> list[Shipment]:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(Shipment).filter(Shipment.user_id == user_id).all()

    def get_shipments_by_courier(self, courier: str) -> list[Shipment]:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(Shipment).filter(Shipment.courier == courier).all()

#Update
    def update_status(self, shipment_id: int, status: str) -> Shipment:
        with Session(self.engine,expire_on_commit=False) as session:
            shipment = session.query(Shipment).filter(Shipment.id == shipment_id).first()
            if shipment:
                shipment.status = status
                session.commit()
            return shipment
        
    def update_courier(self, shipment_id: int, courier: str) -> Shipment:
        with Session(self.engine,expire_on_commit=False) as session:
            shipment = session.query(Shipment).filter(Shipment.id == shipment_id).first()
            if shipment:
                shipment.courier = courier
                session.commit()
            return shipment
        
    def update_tracking_number(self, shipment_id: int, tracking_number: str) -> Shipment:
        with Session(self.engine,expire_on_commit=False) as session:
            shipment = session.query(Shipment).filter(Shipment.id == shipment_id).first()
            if shipment:
                shipment.tracking_number = tracking_number
                session.commit()
            return shipment
        

#Statistic
    def get_recent_shipments(self, limit: int = 10) -> list[Shipment]:
        with Session(self.engine,expire_on_commit=False) as session:
            return session.query(Shipment).order_by(Shipment.id.desc()).limit(limit).all()
    


#Delete

    def delete_shipment(self, shipment_id: int) -> None:
        with Session(self.engine,expire_on_commit=False) as session:
            shipment = session.query(Shipment).filter(Shipment.id == shipment_id).first()
            if shipment:
                session.delete(shipment)
                session.commit()
