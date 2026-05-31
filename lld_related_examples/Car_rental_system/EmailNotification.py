from Notification import Notification

class EmailNotification(Notification):
    def send_notification(self, account):
        print(f"Email to {account.get_name()}: {self.get_content()}")