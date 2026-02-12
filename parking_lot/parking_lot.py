from parking_ticket import ParkingTicket
class ParkingLot:
    _instance = None

    def __init__(self):
        self.id = None
        self.name = None
        self.address = None
        self.parking_rate = None

        self.entrances = None       # dict: str -> Entrance
        self.exits = None           # dict: str -> Exit
        self.spots = {}          # dict: int -> ParkingSpot
        self.tickets = {}         # dict: str -> ParkingTicket
        self.display_boards = []  # list of DisplayBoard

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ParkingLot()
        return cls._instance

    def add_entrance(self, entrance):
        pass

    def add_exit(self, exit):
        pass

    def add_parking_spot(self, spot):
        self.spots[spot.id] = spot

    def add_display_board(self, board):
        for existing_board in self.display_boards:
            if existing_board.id == board.id:
                print(f"Display board with id {board.id} already exists.")
                return
        self.display_boards.append(board)
        print(f"Display board {board.id} added successfully.")

    def get_parking_ticket(self, vehicle): ### work on this
        for spot in self.spots.values():
            if spot.spot_type == vehicle.vehicle_type and spot.is_free:
                spot.assign_vehicle(vehicle)
                ticket = ParkingTicket(vehicle, spot)
                self.tickets[ticket.id] = ticket
                return ticket

        raise Exception("No parking spot available")

    def is_full(self, spot_type):
        for spot in self.spots.values():
            if spot.spot_type == spot_type and spot.is_free:
                return False
        return True
    def add_spot(self,spot):
        self.spots[spot.id]=spot
    
    def get_all_spots(self):
        pass