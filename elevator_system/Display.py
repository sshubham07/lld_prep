from Direction import Direction
from ElevatorState import ElevatorState

class Display:
    def __init__(self):
        self.floor = 0
        self.load = 0
        self.direction = Direction.IDLE
        self.state = ElevatorState.IDLE
        self.maintenance = False
        self.overloaded = False

    def update(self, f, d, load, s, overloaded, maintenance):
        self.floor = f
        self.direction = d
        self.load = load
        self.state = s
        self.overloaded = overloaded
        self.maintenance = maintenance

    def show_elevator_display(self, car_id):
        if self.maintenance:
            msg = "MAINTENANCE"
        elif self.overloaded:
            msg = "OVERLOADED"
        elif self.state == ElevatorState.IDLE:
            msg = "IDLE"
        elif self.state == ElevatorState.UP:
            msg = "UP"
        elif self.state == ElevatorState.DOWN:
            msg = "DOWN"
        else:
            msg = "UNKNOWN"
        print(f"Elevator {car_id} ► Floor: {self.floor} | Dir: {self.direction.name} | Load: {self.load} | State: {msg}")