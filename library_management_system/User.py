from abc import ABC, abstractmethod
from AccountStatus import AccountStatus

class User(ABC):
    def __init__(self, user_id, password, person, card):
        self.id = user_id
        self.password = password
        self.person = person
        self.card = card
        self.status = AccountStatus.ACTIVE

    @abstractmethod
    def reset_password(self):
        pass
