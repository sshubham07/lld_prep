from datetime import datetime
from Package import Package
from Order import Order

class LockerPackage(Package):
    def __init__(self, package_id: str, package_size: float, order: Order,
                 code_valid_days: int, locker_id: str, code: str,
                 package_delivery_time: datetime, delivery_person_id: str):
        super().__init__(package_id, package_size, order)
        self.code_valid_days = code_valid_days
        self.locker_id = locker_id
        self.code = code
        self.package_delivery_time = package_delivery_time
        self.delivery_person_id = delivery_person_id

    def is_valid_code(self) -> bool:
        diff_days = (datetime.now() - self.package_delivery_time).days
        return diff_days <= self.code_valid_days

    def verify_code(self, input_code: str) -> bool:
        if self.code != input_code:
            return False
        if not self.is_valid_code():
            print(f"Code expired for package: {self.package_id}")
            return False
        print(f"Code verified for package: {self.package_id}")
        return True
