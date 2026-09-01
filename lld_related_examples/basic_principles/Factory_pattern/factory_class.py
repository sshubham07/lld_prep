from abc import ABC,abstractmethod
class State(ABC):
    @abstractmethod
    def capital():
        pass

class Maharashtra(State):
    def __init__(self,name):
        self.state_name=name.lower()
    def capital(self):
        print(f"State Capital of {self.state_name} is Mumbai")

class Bihar(State):
    def __init__(self,name):
        self.state_name=name.lower()
    def capital(self):
        print(f"State Capital of {self.state_name} is Patna")
class Punjab(State):
    def __init__(self,name):
        self.state_name=name.lower()
    def capital(self):
        print(f"State Capital of {self.state_name} is Chandigarh")

class Factory:
    _registry={}
    @classmethod
    def register(cls,key,state_cls):
        cls._registry[key]=state_cls
    @classmethod
    def create(cls,name):
        return cls._registry[name.strip().lower()](name)

name = input("Enter state name ")
Factory.register("bihar",Bihar)
Factory.register("Maharashtra",Maharashtra)
Factory.register("Punjab",Punjab)
obj = Factory.create(name)
obj.capital()