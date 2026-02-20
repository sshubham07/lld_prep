from collections import deque
from Door import Door
from Display import Display
from ElevatorPanel import ElevatorPanel
from ElevatorState import ElevatorState
from Direction import Direction

class ElevatorCar:
    MAX_LOAD = 680  # kg

    def __init__(self, id, num_floors):
        self.id = id
        self.current_floor = 0
        self.state = ElevatorState.IDLE
        self.door = Door()
        self.display = Display()
        self.panel = ElevatorPanel(num_floors)
        self.request_queue = deque()
        self.load = 0
        self.overloaded = False
        self.maintenance = False
        self.update_display()

    def get_id(self):
        return self.id

    def get_current_floor(self):
        return self.current_floor

    def get_state(self):
        return self.state

    def get_panel(self):
        return self.panel

    def is_in_maintenance(self):
        return self.maintenance

    def is_overloaded(self):
        return self.overloaded

    def register_request(self, floor):
        if self.maintenance:
            return
        self.request_queue.append(floor)

    def move(self):
        if self.maintenance or self.overloaded or not self.request_queue:
            self.state = ElevatorState.IDLE
            self.update_display()
            return
        target = self.request_queue.popleft()
        if target == self.current_floor:
            self.stop()
            return
        self.state = ElevatorState.UP if target > self.current_floor else ElevatorState.DOWN
        while self.current_floor != target and not self.maintenance and not self.overloaded:
            self.current_floor += 1 if self.state == ElevatorState.UP else -1
            self.update_display()
            self.display.show_elevator_display(self.id)
            print(f"Elevator {self.id+1} passing floor {self.current_floor}")
        self.stop()

    def stop(self):
        if self.maintenance or self.overloaded:
            return
        self.state = ElevatorState.IDLE
        self.update_display()
        self.door.open()
        print(f"Elevator {self.id+1} doors opening at floor {self.current_floor}")

    def enter_maintenance(self):
        self.maintenance = True
        self.state = ElevatorState.MAINTENANCE
        self.door.close()
        self.update_display()
        print(f">>> Elevator {self.id+1} entered MAINTENANCE mode")

    def exit_maintenance(self):
        self.maintenance = False
        self.state = ElevatorState.IDLE
        self.update_display()
        print(f">>> Elevator {self.id+1} exited MAINTENANCE mode, now IDLE")

    def emergency_stop(self):
        self.state = ElevatorState.IDLE
        self.overloaded = False
        self.door.close()
        self.update_display()
        print(f">>> Elevator {self.id+1} EMERGENCY STOP activated!")

    def add_load(self, kg):
        self.load += kg
        if self.load > ElevatorCar.MAX_LOAD:
            self.trigger_overload_alarm()
        self.update_display()

    def remove_load(self, kg):
        self.load -= kg
        if self.load <= ElevatorCar.MAX_LOAD:
            self.clear_overload_alarm()
        self.update_display()

    def trigger_overload_alarm(self):
        self.overloaded = True
        print(f"!!! Elevator {self.id+1} OVERLOAD ALARM !!!")

    def clear_overload_alarm(self):
        self.overloaded = False
        print(f"Overload cleared for Elevator {self.id+1}.")

    def update_display(self):
        if self.state == ElevatorState.UP:
            dir = Direction.UP
        elif self.state == ElevatorState.DOWN:
            dir = Direction.DOWN
        else:
            dir = Direction.IDLE
        self.display.update(self.current_floor, dir, self.load, self.state, self.overloaded, self.maintenance)

    def get_display(self):
        return self.display

    def get_door(self):
        return self.door