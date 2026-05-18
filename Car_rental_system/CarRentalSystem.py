from CarRentalBranch import CarRentalBranch

class CarRentalSystem:
    _instance = None

    def __init__(self):
        if CarRentalSystem._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.name = ""
            self.branches = []
            CarRentalSystem._instance = self

    @staticmethod
    def get_instance():
        if CarRentalSystem._instance is None:
            CarRentalSystem()
        return CarRentalSystem._instance

    def add_new_branch(self, branch: CarRentalBranch):
        self.branches.append(branch)

    def get_branches(self):
        return self.branches