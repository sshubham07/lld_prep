from Calendar import Calendar
from RSVPStatus import RSVPStatus

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.calendar = Calendar()

    def respond_invitation(self, meeting: 'Meeting', response: str):
        meeting.update_participant_status(self, RSVPStatus(response))
        print(f"  · {self.name} responded: {response}")
        if response == RSVPStatus.REJECTED.value:
            self.calendar.remove_meeting(meeting)
        elif response == RSVPStatus.ACCEPTED.value:
            self.calendar.add_meeting(meeting)

    def view_meetings(self) -> list['Meeting']:
        return self.calendar.get_meetings()

    def get_name(self) -> str:
        return self.name

    def get_calendar(self) -> Calendar:
        return self.calendar
