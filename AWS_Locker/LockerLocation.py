from typing import List
from datetime import datetime
from Locker import Locker

class LockerLocation:
    def __init__(self, name: str, longitude: float, latitude: float, open_time: datetime, close_time: datetime):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.open_time = open_time
        self.close_time = close_time
        self.lockers: List[Locker] = []

    def add_locker(self, locker: Locker):
        self.lockers.append(locker)
