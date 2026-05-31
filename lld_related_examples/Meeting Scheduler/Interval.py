from datetime import datetime

class Interval:
    def __init__(self, start_time: datetime, end_time: datetime):
        self.start_time = start_time
        self.end_time = end_time

    def get_start_time(self) -> datetime:
        return self.start_time

    def get_end_time(self) -> datetime:
        return self.end_time

    # Check if intervals overlap
    def overlaps(self, other: 'Interval') -> bool:
        return not (self.end_time <= other.start_time or self.start_time >= other.end_time)
