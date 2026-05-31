from Notification import Notification

class EmailNotification(Notification):
    def send_notification(self, person):
        print(f"Email sent to {person.email}: {self.content}")
