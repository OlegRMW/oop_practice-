from abc import ABC, abstractmethod

class Plant(ABC):
    @abstractmethod
    def calculate_growth(self):
        pass

    @abstractmethod
    def calculate_water_needs(self):
        pass