from Interval import Interval

class MeetingRoom:
    def __init__(self, id: int, capacity: int):
        self.id = id
        self.capacity = capacity
        self.booked_intervals: list[Interval] = []

    def is_available_for(self, interval: Interval, request_capacity: int) -> bool:
        if request_capacity > self.capacity:
            return False
        return all(not iv.overlaps(interval) for iv in self.booked_intervals)

    def book_interval(self, interval: Interval):
        self.booked_intervals.append(interval)

    def release_interval(self, interval: Interval):
        self.booked_intervals = [
            iv for iv in self.booked_intervals
            if iv.get_start_time() != interval.get_start_time() or iv.get_end_time() != interval.get_end_time()
        ]

    def get_id(self) -> int:
        return self.id

    def get_capacity(self) -> int:
        return self.capacity

    def __str__(self) -> str:
        return f"Room {self.id} (cap: {self.capacity})"
