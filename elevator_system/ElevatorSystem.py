from collections import deque
from Building import Building
from Direction import Direction
from ElevatorState import ElevatorState

class FloorRequest:
    def __init__(self, floor, dir):
        self.floor = floor
        self.dir = dir

class ElevatorSystem:
    _system = None

    def __init__(self, floors, cars, num_panels, num_displays):
        self.building = Building(floors, cars, num_panels, num_displays)
        self.hall_requests = deque()

    @classmethod
    def get_instance(cls, floors, cars, num_panels, num_displays):
        if cls._system is None:
            cls._system = ElevatorSystem(floors, cars, num_panels, num_displays)
        return cls._system

    def get_cars(self):
        return self.building.get_cars()

    def get_building(self):
        return self.building

    def call_elevator(self, floor_num, dir):
        self.hall_requests.append(FloorRequest(floor_num, dir))

    def get_nearest_idle_car(self, floor):
        best = None
        min_dist = float('inf')
        for car in self.building.get_cars():
            if (car.get_state() == ElevatorState.IDLE and
                not car.is_in_maintenance() and
                not car.is_overloaded()):
                dist = abs(car.get_current_floor() - floor)
                if dist < min_dist:
                    min_dist = dist
                    best = car
        return best

    def dispatcher(self):
        while self.hall_requests:
            req = self.hall_requests.popleft()
            car = self.get_nearest_idle_car(req.floor)
            if car is None:
                print("No idle car available; re-queueing request")
                self.hall_requests.append(req)
                break
            print(f"Dispatching Elevator {car.get_id()+1} to floor {req.floor}")
            car.register_request(req.floor)
            car.move()

    def monitoring(self):
        for car in self.get_cars():
            car.get_display().show_elevator_display(car.get_id() + 1)  # +1 for user-friendly ID