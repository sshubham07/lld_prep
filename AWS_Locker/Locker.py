from typing import Optional
from LockerSize import LockerSize
from LockerState import LockerState
from LockerPackage import LockerPackage

class Locker:
    def __init__(self, locker_id: str, locker_size: LockerSize, location_id: str):
        self.locker_id = locker_id
        self.locker_size = locker_size
        self.location_id = location_id
        self.locker_state = LockerState.AVAILABLE
        self.current_package: Optional[LockerPackage] = None

    def add_package(self, pkg: LockerPackage) -> bool:
        if self.locker_state != LockerState.AVAILABLE:
            print(f"Locker {self.locker_id} is not available.")
            return False
        self.current_package = pkg
        self.locker_state = LockerState.BOOKED
        print(f"Package {pkg.package_id} added to locker {self.locker_id}")
        return True

    def remove_package(self, code: str) -> bool:
        if self.locker_state != LockerState.BOOKED or not self.current_package:
            print(f"Locker {self.locker_id} has no package to remove.")
            return False
        if not self.current_package.verify_code(code):
            print(f"Failed to verify code for package in locker {self.locker_id}")
            return False
        print(f"Package {self.current_package.package_id} removed from locker {self.locker_id}")
        self.current_package = None
        self.locker_state = LockerState.AVAILABLE
        return True
