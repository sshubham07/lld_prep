from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self):
        self.notification_id = 0
        self.created_on = None
        self.content = ""

    @abstractmethod
    def send_notification(self, person):
        pass
