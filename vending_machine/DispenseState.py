from State import State

class DispenseState(State):
    def insertMoney(self, machine, amount):
        print("[DispenseState] insertMoney: Currently dispensing. Please wait.")

    def selectProduct(self, machine, rackNumber):
        print("[DispenseState] selectProduct: Already dispensing. Please wait.")
