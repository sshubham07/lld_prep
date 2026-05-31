from abc import ABC, abstractmethod
from Person import Person
from AccountStatus import AccountStatus

class Account(Person, ABC):
    def __init__(self):
        super().__init__()
        self._account_id = ""
        self._password = ""
        self._status = AccountStatus.ACTIVE

    def get_account_id(self): return self._account_id
    def set_account_id(self, account_id): self._account_id = account_id

    def get_status(self): return self._status
    def set_status(self, status): self._status = status

    def set_password(self, password): self._password = password
    def get_password(self): return self._password

    @abstractmethod
    def reset_password(self): pass