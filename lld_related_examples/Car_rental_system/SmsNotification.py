from Notification import Notification

class SmsNotification(Notification):
    def send_notification(self, account):
        print(f"SMS to {account.get_name()}: {self.get_content()}")