from abc import ABC,abstractmethod
class Coffee:
    def cost(self):
        print(f"Inside Base coffee ")
        return 100

class CoffeeDecorator(ABC):
    def __init__(self,coffee):
        self.coffee = coffee
    @abstractmethod
    def cost(self):
        pass

class MilkAdd(CoffeeDecorator):
    def cost(self):
        print(f"Inside Milk Add and coffee obj is {self.coffee.__class__.__name__}")
        return self.coffee.cost()+20
    
class ChocolateAdd(CoffeeDecorator):
    def cost(self):
        print(f"Inside Chocolate Add and coffee obj is {self.coffee.__class__.__name__}")
        return self.coffee.cost()+30

class IceAdd(CoffeeDecorator):
    def cost(self):
        print(f"Inside Milk Add and coffee obj is {self.coffee.__class__.__name__}")
        return self.coffee.cost()+10

total = MilkAdd(ChocolateAdd(IceAdd(Coffee()))).cost()
print(total)