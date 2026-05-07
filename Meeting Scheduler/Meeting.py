from typing import List, Dict
from Interval import Interval
from MeetingRoom import MeetingRoom
from RSVPStatus import RSVPStatus

class Meeting:
    _next_id = 1

    def __init__(self, participants: List['User'], interval: Interval, room: MeetingRoom, subject: str):
        self.id = Meeting._next_id
        Meeting._next_id += 1

        self.participant_status: Dict['User', RSVPStatus] = {user: RSVPStatus.PENDING for user in participants}
        self.interval = interval
        self.room = room
        self.subject = subject

    def add_participants(self, participants: List['User']):
        for user in participants:
            if user not in self.participant_status:
                self.participant_status[user] = RSVPStatus.PENDING

    def update_participant_status(self, user: 'User', status: RSVPStatus):
        if user in self.participant_status:
            self.participant_status[user] = status

    def get_accepted_participants(self) -> List['User']:
        return [user for user, status in self.participant_status.items() if status == RSVPStatus.ACCEPTED]

    def get_pending_participants(self) -> List['User']:
        return [user for user, status in self.participant_status.items() if status == RSVPStatus.PENDING]

    def get_rejected_participants(self) -> List['User']:
        return [user for user, status in self.participant_status.items() if status == RSVPStatus.REJECTED]

    def get_interval(self) -> Interval:
        return self.interval

    def get_room(self) -> MeetingRoom:
        return self.room

    def get_subject(self) -> str:
        return self.subject
