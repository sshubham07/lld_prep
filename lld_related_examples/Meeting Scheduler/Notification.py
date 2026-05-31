from datetime import datetime

class Notification:
    def __init__(self, notification_id: int, content: str, creation_date: datetime):
        self.notification_id = notification_id
        self.content = content
        self.creation_date = creation_date

    def send_invite(self, user: 'User', meeting: 'Meeting'):
        print(f"  - Notification sent to {user.get_name()} for meeting: {meeting.get_subject()}")

    def send_cancel_notification(self, user: 'User', meeting: 'Meeting'):
        print(f"  - Cancellation sent to {user.get_name()} for meeting: {meeting.get_subject()}")
