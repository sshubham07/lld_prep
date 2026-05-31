from abc import ABC, abstractmethod
from datetime import datetime

class Notification(ABC):
    def __init__(self, notification_id, content):
        self.notification_id = notification_id
        self.content = content
        self.created = datetime.now()

    @abstractmethod
    def send_notification(self):
        pass
