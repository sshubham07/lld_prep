from Notification import Notification

class PostalNotification(Notification):
    def __init__(self, notification_id, content, address):
        super().__init__(notification_id, content)
        self.address = address

    def send_notification(self):
        print(f"Postal notification to {self.address}: {self.content}")
        return True
