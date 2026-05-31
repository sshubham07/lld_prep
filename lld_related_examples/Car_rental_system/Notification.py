from abc import ABC, abstractmethod
from datetime import datetime

class Notification(ABC):
    def __init__(self):
        self.notification_id = None
        self.created_on = datetime.now()
        self._content = ""

    def set_content(self, content):
        self._content = content

    def get_content(self):
        return self._content

    @abstractmethod
    def send_notification(self, account):
        pass