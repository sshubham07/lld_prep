from abc import ABC, abstractmethod
from typing import List
from Vehicle import Vehicle

class Search(ABC):
    @abstractmethod
    def search_by_type(self, type_str: str) -> List[Vehicle]:
        pass

    @abstractmethod
    def search_by_model(self, model: str) -> List[Vehicle]:
        pass