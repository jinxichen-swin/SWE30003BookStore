from database.connection import Base, engine
from database.models.user import User
from managers.user_manager import UserManager

Base.metadata.create_all(engine)

manager = UserManager(engine)

user = manager.register_user(
    firstname="Max",
    surname="Chen",
    email="114514@gmail.com",
    password="12345678"
)
print("Created:", user.id, user.email)


user=manager.login("13131313", "12345678")
if user:
    print("Login successful:", user.id, user.email)
else:
    print("Login failed")

user=manager.login("114514@gmail.com", "123456781")
if user:
    print("Login successful:", user.id, user.email)
else:
    print("Login failed")

user=manager.login("114514@gmail.com", "12345678")
if user:
    print("Login successful:", user.id, user.email)
else:
    print("Login failed")


# s = manager.get_shipment(shipment.id)
# print("Got:", s.address)

# manager.update_courier(shipment.id, "FedEx")
# s = manager.get_shipment(shipment.id)
# print("Updated courier:", s.courier)

# manager.update_status(shipment.id, "shipped")
# s = manager.get_shipment(shipment.id)
# print("Updated status:", s.status)

# manager.delete_shipment(shipment.id)
# print("Deleted")