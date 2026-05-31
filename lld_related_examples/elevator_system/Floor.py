from HallPanel import HallPanel
from Display import Display

class Floor:
    def __init__(self, floor_number, num_panels, num_displays, top_floor):
        self.floor_number = floor_number
        self.panels = [HallPanel(floor_number, top_floor) for _ in range(num_panels)]
        self.displays = [Display() for _ in range(num_displays)]

    def get_floor_number(self):
        return self.floor_number

    def get_panels(self):
        return self.panels

    def get_panel(self, index):
        return self.panels[index]

    def get_displays(self):
        return self.displays

    def get_display(self, index):
        return self.displays[index]