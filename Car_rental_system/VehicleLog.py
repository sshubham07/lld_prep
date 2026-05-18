from datetime import datetime
from VehicleLogType import VehicleLogType

class VehicleLog:
    def __init__(self, log_id: int, log_type: VehicleLogType, description: str):
        self.log_id = log_id
        self.log_type = log_type
        self.description = description
        self.creation_date = datetime.now()