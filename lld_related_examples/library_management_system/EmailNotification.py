from Notification import Notification

class EmailNotification(Notification):
    def __init__(self, notification_id, content, email):
        super().__init__(notification_id, content)
        self.email = email

    def send_notification(self):
        print(f"Email notification to {self.email}: {self.content}")
        return True
