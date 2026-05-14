from abc import ABC, abstractmethod

class Search(ABC):
    @abstractmethod
    def search_movie_title(self, title):
        pass

    @abstractmethod
    def search_movie_language(self, language):
        pass

    @abstractmethod
    def search_movie_genre(self, genre):
        pass

    @abstractmethod
    def search_movie_release_date(self, date):
        pass
