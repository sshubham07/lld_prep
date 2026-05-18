import uuid
from Account import Account

class Customer(Account):
    def __init__(self):
        super().__init__()
        self._license_number = ""
        self._license_expiry = None

    def set_license_number(self, number): self._license_number = number
    def get_license_number(self): return self._license_number

    def set_license_expiry(self, expiry_date): self._license_expiry = expiry_date
    def get_license_expiry(self): return self._license_expiry

    def reset_password(self):
        self.set_password(str(uuid.uuid4()))
        return True