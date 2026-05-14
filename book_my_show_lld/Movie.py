class Movie:
    def __init__(self, title, genre, release_date, language, duration, shows=None):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.language = language
        self.duration = duration
        self.shows = shows if shows is not None else []
