from MeetingRoom import MeetingRoom
from User import User
from MeetingScheduler import MeetingScheduler
from Interval import Interval
from datetime import datetime

def header(title: str):
    print("\n==============================")
    print(f"▶ {title}")
    print("==============================\n")

def arrow(msg: str):
    print(f"→ {msg}")

def get_interval(year, month, day, start_hour, start_min, end_hour, end_min) -> Interval:
    start = datetime(year, month, day, start_hour, start_min, 0)
    end = datetime(year, month, day, end_hour, end_min, 0)
    return Interval(start, end)

def main():
    # Set up rooms
    roomA = MeetingRoom(1, 4)
    roomB = MeetingRoom(2, 8)
    rooms = [roomA, roomB]

    # Set up users
    alice = User("Alice", "alice@email.com")
    bob = User("Bob", "bob@email.com")
    charlie = User("Charlie", "charlie@email.com")
    participants = [alice, bob, charlie]

    # Set up scheduler
    scheduler = MeetingScheduler(alice, rooms)

    # Scenario 1
    header("Scenario 1: Schedule a Meeting (Random Accept/Reject)")
    arrow("Scheduling meeting \"Design Review\" for Alice, Bob, Charlie...")
    interval1 = get_interval(2025, 7, 10, 10, 0, 11, 0)
    meeting1 = scheduler.schedule_meeting(participants, interval1, "Design Review")

    # Scenario 2
    header("Scenario 2: Schedule Another Meeting (Random Accept/Reject)")
    arrow("Scheduling meeting \"Sprint Planning\" for Alice, Bob, Charlie...")
    interval2 = get_interval(2025, 7, 10, 12, 0, 13, 0)
    meeting2 = scheduler.schedule_meeting(participants, interval2, "Sprint Planning")

    # Scenario 3
    header("Scenario 3: Cancel Meeting")
    arrow("Cancelling meeting \"Design Review\"...")
    if meeting1 is not None:
        scheduler.cancel_meeting(meeting1)

if __name__ == "__main__":
    main()
