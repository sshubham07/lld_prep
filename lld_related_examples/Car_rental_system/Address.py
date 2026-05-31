class Address:
    def __init__(self, street, city, state, zip_code, country):
        self._street_address = street
        self._city = city
        self._state = state
        self._zip_code = zip_code
        self._country = country

    def get_street_address(self): return self._street_address
    def get_city(self): return self._city
    def get_state(self): return self._state
    def get_zip_code(self): return self._zip_code
    def get_country(self): return self._country

    def __str__(self):
        return f"{self._street_address}, {self._city}, {self._state} {self._zip_code}, {self._country}"