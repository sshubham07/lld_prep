from typing import List, Dict
from Search import Search
from Vehicle import Vehicle

class VehicleCatalog(Search):
    def __init__(self):
        self.vehicle_types: Dict[str, List[Vehicle]] = {}
        self.vehicle_models: Dict[str, List[Vehicle]] = {}

    def add_vehicle(self, vehicle: Vehicle):
        type_name = vehicle.__class__.__name__.upper()
        self.vehicle_types.setdefault(type_name, []).append(vehicle)

        model = vehicle.get_model()
        self.vehicle_models.setdefault(model, []).append(vehicle)

    def search_by_type(self, type_str: str) -> List[Vehicle]:
        return self.vehicle_types.get(type_str.upper(), [])

    def search_by_model(self, model: str) -> List[Vehicle]:
        return self.vehicle_models.get(model, [])