class City:
    def __init__(self, name, state, zip_code, cinemas=None):
        self.name = name
        self.state = state
        self.zip_code = zip_code
        self.cinemas = cinemas if cinemas is not None else []
