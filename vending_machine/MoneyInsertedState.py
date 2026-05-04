from State import State

class MoneyInsertedState(State):
    def insertMoney(self, machine, amount):
        print(f"[MoneyInsertedState] insertMoney: adding ${amount:.2f} to current amount.")
        machine.addToCurrentAmount(amount)
        print(f"[MoneyInsertedState] Total amount = ${machine.getCurrentAmount():.2f}.")

    def selectProduct(self, machine, rackNumber):
        print(f"[MoneyInsertedState] selectProduct: rack {rackNumber} selected.")
        rack = machine.getInventory().getRack(rackNumber)
        if rack is None or rack.isEmpty():
            print("[MoneyInsertedState] Selected rack is empty or does not exist. Refunding...")
            machine.refund()
            return

        product = rack.peekProduct()
        price = product.getPrice()
        paid = machine.getCurrentAmount()
        print(f"[MoneyInsertedState] Product price = ${price:.2f}, paid = ${paid:.2f}.")

        if paid < price:
            print("[MoneyInsertedState] Insufficient funds. Refunding...")
            machine.refund()
            return

        print("[MoneyInsertedState] Sufficient funds. Proceeding to dispense.")
        machine.setSelectedRack(rackNumber)
        machine.setState(machine.getDispenseState())
        machine.dispenseProduct()
