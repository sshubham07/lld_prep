from Person import Person

class Driver(Person):
    def __init__(self):
        super().__init__()
        self._driver_id = None

    def get_driver_id(self):
        return self._driver_id

    def set_driver_id(self, driver_id):
        self._driver_id = driver_id