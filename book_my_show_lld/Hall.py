class Hall:
    def __init__(self, hall_id, shows=None):
        self.hall_id = hall_id
        self.shows = shows if shows is not None else []

    def find_current_shows(self):
        return self.shows
