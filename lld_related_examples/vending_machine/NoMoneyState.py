from State import State

class NoMoneyState(State):
    def insertMoney(self, machine, amount):
        print(f"[NoMoneyState] insertMoney: received ${amount:.2f}")
        machine.addToCurrentAmount(amount)
        print(f"[NoMoneyState] Current amount = ${machine.getCurrentAmount():.2f}. You may now select a product.")
        machine.setState(machine.getMoneyInsertedState())

    def selectProduct(self, machine, rackNumber):
        print("[NoMoneyState] selectProduct: No money inserted. Please insert cash first.")
