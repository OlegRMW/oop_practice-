import random

class Ninja:
    
    def __init__(self, name: str, health = 100) -> None:
        self.__name = name 
        self.__health = health 
        
    def set_name(self, new_name: str) -> None:
        self.__name = new_name
        print(f'имя персонажа измененно на: {new_name}')
        
    def throw_shuriken(self) -> None:
        return random.randint(10, 30)
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, health: int):
        self.__health = health
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: int):
        self.__name = name
    


