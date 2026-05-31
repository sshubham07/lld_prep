from Button import Button

class EmergencyButton(Button):
    def get_pressed(self):
        return self.pressed

    def set_pressed(self, val):
        self.pressed = val

    def is_pressed(self):
        return self.pressed