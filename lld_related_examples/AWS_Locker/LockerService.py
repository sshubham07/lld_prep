from typing import List, Optional
from LockerLocation import LockerLocation
from LockerState import LockerState
from LockerSize import LockerSize
from Locker import Locker
from Order import Order
from LockerPackage import LockerPackage

class LockerService:
    _instance: Optional['LockerService'] = None

    def __init__(self):
        self.locations: List[LockerLocation] = []

    @classmethod
    def get_instance(cls) -> 'LockerService':
        if cls._instance is None:
            cls._instance = LockerService()
        return cls._instance

    def add_location(self, loc: LockerLocation):
        self.locations.append(loc)

    def get_locations(self) -> List[LockerLocation]:
        return self.locations

    def find_locker_by_id(self, locker_id: str) -> Optional[Locker]:
        for loc in self.locations:
            for locker in loc.lockers:
                if locker.locker_id == locker_id:
                    return locker
        return None

    def request_return(self, order: Order) -> bool:
        print(f"Return request received for order: {order.order_id}")
        return True

    def request_locker(self, size: LockerSize) -> Optional[Locker]:
        for loc in self.locations:
            for locker in loc.lockers:
                if locker.locker_state == LockerState.AVAILABLE and locker.locker_size == size:
                    print(f"Found available locker: {locker.locker_id}")
                    return locker
        print("No available lockers at the moment.")
        return None

    def verify_otp(self, pkg: LockerPackage, code: str) -> bool:
        return pkg.verify_code(code)
