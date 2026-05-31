from Search import Search
from collections import defaultdict

class Catalog(Search):
    def __init__(self):
        self.movie_titles = defaultdict(list)
        self.movie_languages = defaultdict(list)
        self.movie_genres = defaultdict(list)
        self.movie_release_dates = defaultdict(list)

    def search_movie_title(self, title):
        return self.movie_titles.get(title, [])

    def search_movie_language(self, language):
        return self.movie_languages.get(language, [])

    def search_movie_genre(self, genre):
        return self.movie_genres.get(genre, [])

    def search_movie_release_date(self, date):
        return self.movie_release_dates.get(date, [])
