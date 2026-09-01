from abc import ABC,abstractmethod
class State(ABC):
    @abstractmethod
    def state_name():
        pass

class Maharashtra(State):
    def __init__(self,name):
        self.state_name=name
    def state_name(self):
        print(f"State Name={self.state_name}")

class Bihar(State):
    def __init__(self,name):
        self.state_name=name
    def state_name(self):
        print(f"State Name={self.state_name}")
def make_state_obj(name):
    if name.lower()=="bihar":
        return Bihar(name)
    else:
        return Maharashtra(name)
name = input("Enter state name ")
obj = make_state_obj(name)
print(obj.state_name)