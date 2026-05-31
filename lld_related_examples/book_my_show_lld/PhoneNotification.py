from Notification import Notification

class PhoneNotification(Notification):
    def send_notification(self, person):
        print(f"SMS sent to {person.phone}: {self.content}")
