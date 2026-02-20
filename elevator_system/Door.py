from DoorState import DoorState

class Door:
    def __init__(self):
        self.state = DoorState.CLOSED

    def open(self):
        self.state = DoorState.OPEN

    def close(self):
        self.state = DoorState.CLOSED

    def is_open(self):
        return self.state == DoorState.OPEN

    def get_state(self):
        return self.state