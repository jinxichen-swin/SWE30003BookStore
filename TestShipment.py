from database.connection import Base, engine
from database.models.shipment import Shipment
from managers.shipment_manager import ShipmentManager

Base.metadata.create_all(engine)

manager = ShipmentManager(engine)

shipment = manager.create_shipment(
    order_id=1,
    user_id=1,
    address="123 Test St",
    courier="DHL",
    tracking_number="ABC123"
)
print("Created:", shipment.id, shipment.status)

s = manager.get_shipment(shipment.id)
print("Got:", s.address)

manager.update_courier(shipment.id, "FedEx")
s = manager.get_shipment(shipment.id)
print("Updated courier:", s.courier)

manager.update_status(shipment.id, "shipped")
s = manager.get_shipment(shipment.id)
print("Updated status:", s.status)

manager.delete_shipment(shipment.id)
print("Deleted")