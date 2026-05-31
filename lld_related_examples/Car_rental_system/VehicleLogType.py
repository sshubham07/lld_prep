from enum import Enum

class VehicleLogType(Enum):
    ACCIDENT = 1
    FUELING = 2
    CLEANING_SERVICE = 3
    OIL_CHANGE = 4
    REPAIR = 5
    OTHER = 6