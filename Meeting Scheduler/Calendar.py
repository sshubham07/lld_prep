class Calendar:
    def __init__(self):
        self.meetings: list['Meeting'] = []

    def add_meeting(self, meeting: 'Meeting'):
        if meeting not in self.meetings:
            self.meetings.append(meeting)

    def remove_meeting(self, meeting: 'Meeting'):
        if meeting in self.meetings:
            self.meetings.remove(meeting)

    def get_meetings(self) -> list['Meeting']:
        return self.meetings
