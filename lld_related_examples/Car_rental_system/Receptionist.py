import uuid
from Account import Account
from AccountStatus import AccountStatus

class Receptionist(Account):
    def __init__(self):
        super().__init__()
        self._date_joined = None
        self._customer_list = []
        self.set_status(AccountStatus.ACTIVE)

    def search_customer(self, name):
        return [c for c in self._customer_list if c.get_name() and name in c.get_name()]

    def add_customer(self, customer):
        self._customer_list.append(customer)

    @staticmethod
    def add_reservation(all_reservations, reservation):
        all_reservations.append(reservation)
        return True

    @staticmethod
    def cancel_reservation(all_reservations, reservation):
        if reservation in all_reservations:
            all_reservations.remove(reservation)
            return True
        return False

    def reset_password(self):
        self.set_password(str(uuid.uuid4()))
        return True