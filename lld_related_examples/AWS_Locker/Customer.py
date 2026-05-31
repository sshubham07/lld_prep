from Order import Order
from Notification import Notification

class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def place_order(self, order: Order):
        print(f"Customer {self.customer_id} placed order {order.order_id}")

    def request_return(self, order: Order):
        print(f"Customer {self.customer_id} requested return for order {order.order_id}")

    def receive_notification(self, notification: Notification):
        print(f"Customer {self.customer_id} received notification for order {notification.order_id}")
