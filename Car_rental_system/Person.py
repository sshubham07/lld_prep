from abc import ABC

class Person(ABC):
    def __init__(self):
        self._name = ""
        self._address = None
        self._email = ""
        self._phone_number = ""

    def set_name(self, name): self._name = name
    def get_name(self): return self._name

    def set_email(self, email): self._email = email
    def get_email(self): return self._email

    def set_phone_number(self, phone_number): self._phone_number = phone_number
    def get_phone_number(self): return self._phone_number

    def set_address(self, address): self._address = address
    def get_address(self): return self._address