from ElevatorButton import ElevatorButton
from DoorButton import DoorButton
from EmergencyButton import EmergencyButton

class ElevatorPanel:
    def __init__(self, num_floors):
        self.floor_buttons = [ElevatorButton(i) for i in range(num_floors)]
        self.open_button = DoorButton()
        self.close_button = DoorButton()
        self.emergency_button = EmergencyButton()

    def get_floor_buttons(self):
        return self.floor_buttons

    def get_open_button(self):
        return self.open_button

    def get_close_button(self):
        return self.close_button

    def get_emergency_button(self):
        return self.emergency_button

    def enter_emergency(self):
        self.emergency_button.press_down()

    def exit_emergency(self):
        self.emergency_button.reset()