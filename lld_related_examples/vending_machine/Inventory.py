class Inventory:
    def __init__(self):
        self._racks = {}

    def addRack(self, rack):
        self._racks[rack.getRackNumber()] = rack

    def getRack(self, rackNumber):
        return self._racks.get(rackNumber)

    def allRacks(self):
        return self._racks.values()
