from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insertMoney(self, machine, amount):
        pass

    @abstractmethod
    def selectProduct(self, machine, rackNumber):
        pass
