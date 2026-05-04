from NoMoneyState import NoMoneyState
from MoneyInsertedState import MoneyInsertedState
from DispenseState import DispenseState
from Inventory import Inventory

class VendingMachine:
    _instance = None

    def __init__(self):
        self._noMoneyState = NoMoneyState()
        self._moneyInsertedState = MoneyInsertedState()
        self._dispenseState = DispenseState()
        self._currentState = self._noMoneyState
        self._currentAmount = 0.0
        self._selectedRack = -1
        self._inventory = Inventory()

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = VendingMachine()
        return cls._instance

    def getNoMoneyState(self):
        return self._noMoneyState

    def getMoneyInsertedState(self):
        return self._moneyInsertedState

    def getDispenseState(self):
        return self._dispenseState

    def setState(self, state):
        print(f">> Transition: {type(self._currentState).__name__} -> {type(state).__name__}")
        self._currentState = state

    def getCurrentAmount(self):
        return self._currentAmount

    def addToCurrentAmount(self, amount):
        self._currentAmount += amount

    def getInventory(self):
        return self._inventory

    def setSelectedRack(self, rackNumber):
        self._selectedRack = rackNumber

    def insertMoney(self, amount):
        self._currentState.insertMoney(self, amount)

    def selectProduct(self, rackNumber):
        self._currentState.selectProduct(self, rackNumber)

    def dispenseProduct(self):
        print("[DispenseState] dispenseProduct: Dispensing now...")
        rack = self._inventory.getRack(self._selectedRack)
        if not rack:
            return
        product = rack.peekProduct()
        print(f"Dispensing {product.getName()}. Enjoy!")
        rack.dispenseOne()
        change = self._currentAmount - product.getPrice()
        if change > 0:
            print(f"Returning change: ${change:.2f}")
        self._reset()

    def refund(self):
        print(f"Refunding full amount: ${self._currentAmount:.2f}")
        self._reset()

    def _reset(self):
        self._currentAmount = 0
        self._selectedRack = -1
        self.setState(self._noMoneyState)

    def addRack(self, rack):
        self._inventory.addRack(rack)

    def loadProduct(self, rackNumber, product, qty):
        rack = self._inventory.getRack(rackNumber)
        if rack is None:
            print(f"[Admin] No such rack: {rackNumber}")
            return
        rack.loadProduct(product, qty)
        print(f"[Admin] Loaded {qty} × {product.getName()} into rack {rackNumber}")

    def showInventory(self):
        print("\n=== Inventory Status ===")
        for rack in self._inventory.allRacks():
            print(rack)
        print("========================\n")
