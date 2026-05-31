from Meeting import Meeting
from Notification import Notification
from datetime import datetime
import random

class MeetingScheduler:
    def __init__(self, organizer: 'User', rooms: list['MeetingRoom']):
        self.organizer = organizer
        self.calendar = organizer.get_calendar()
        self.rooms = rooms

    def schedule_meeting(self, users: list['User'], interval: 'Interval', subject: str) -> 'Meeting | None':
        room = self.check_rooms_availability(len(users), interval)
        if room is None:
            print("✗ No room available for the interval.")
            return None

        self.book_room(room, interval)
        meeting = Meeting(users, interval, room, subject)

        for user in users:
            user.get_calendar().add_meeting(meeting)
        self.organizer.get_calendar().add_meeting(meeting)

        notification = Notification(1, f"Meeting Invitation: {subject}", datetime.now())
        for user in users:
            notification.send_invite(user, meeting)
            response = random.choice(["ACCEPTED", "REJECTED"])
            user.respond_invitation(meeting, response)

        print("✔ Meeting scheduled successfully!\n")
        return meeting

    def cancel_meeting(self, meeting: Meeting) -> bool:
        self.release_room(meeting.get_room(), meeting.get_interval())
        for user in meeting.get_accepted_participants():
            user.get_calendar().remove_meeting(meeting)
            notification = Notification(2, f"Meeting Cancelled: {meeting.get_subject()}", datetime.now())
            notification.send_cancel_notification(user, meeting)

        print("✔ Meeting cancelled!\n")
        return True

    def check_rooms_availability(self, capacity: int, interval: 'Interval') -> 'MeetingRoom | None':
        for room in self.rooms:
            if room.is_available_for(interval, capacity):
                return room
        return None

    def book_room(self, room: 'MeetingRoom', interval: 'Interval') -> bool:
        room.book_interval(interval)
        return True

    def release_room(self, room: 'MeetingRoom', interval: 'Interval') -> bool:
        room.release_interval(interval)
        return True
