class Notification:
    def __init__(self, customer_id: str, order_id: str, locker_id: str, code: str):
        self.customer_id = customer_id
        self.order_id = order_id
        self.locker_id = locker_id
        self.code = code

    def send(self):
        print(f"Notification sent to customer {self.customer_id}: "
              f"Your order {self.order_id} has been placed in locker {self.locker_id}. "
              f"Pickup code: {self.code}")
