from VendingMachine import VendingMachine
from Rack import Rack
from Product import Product
from ProductType import ProductType

if __name__ == "__main__":
    vm = VendingMachine.getInstance()

    vm.addRack(Rack(1))
    vm.addRack(Rack(2))
    vm.addRack(Rack(3))

    choc = Product(101, "Chocolate Bar", 1.50, ProductType.CHOCOLATE)
    snack = Product(102, "Potato Chips", 2.00, ProductType.SNACK)
    bev = Product(103, "Soda Can", 2.50, ProductType.BEVERAGE)

    vm.loadProduct(1, choc, 5)
    vm.loadProduct(2, snack, 3)
    vm.loadProduct(3, bev, 2)

    vm.showInventory()

    print("========== Scenario 1: Exact Payment ==========")
    vm.insertMoney(1.50)
    vm.selectProduct(1)

    print("========== Scenario 2: Overpayment & Change ==========")
    vm.insertMoney(3.00)
    vm.selectProduct(2)

    print("========== Scenario 3: Underpayment & Refund ==========")
    vm.insertMoney(1.00)
    vm.selectProduct(3)

    print("========== Scenario 4: Deplete Rack 3 & Retry ==========")
    vm.insertMoney(5.00)
    vm.selectProduct(3)
    vm.insertMoney(2.50)
    vm.selectProduct(3)
    vm.insertMoney(2.50)
    vm.selectProduct(3)

    vm.showInventory()
