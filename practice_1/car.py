from driver import Driver

class Car:
    def __init__(self, brand, reg, driver):
        self.__mileage = 0 
        self.__brand = brand 
        self.__reg = reg 
        self.__driver = driver
    
    def __repr__(self):
        return f"'{self.brand} - {self.reg}'"
    
    def assign_driver(self, driver: Driver):
        self.driver = driver 
        print(f'Теперь {self.driver} водитель авто {self.reg}')
    
    def remove_driver(self):
        if self.driver != '':
            old_driver = self.driver
            self.driver = '' 
            print(f'Водитель {old_driver} снят с авто {self.reg}')
        else:
            print('Авто без водителя, сначала добавьте водителя')    
        
    def increase_mileage(self, value):
        self.mileage += value 
        print(f'Пробег авто {self} увеличен на {value}, текущий пробег: {self.mileage}')
        
    @property
    def mileage(self):
        return self.__mileage
    
    @mileage.setter
    def mileage(self, value):
        self.__mileage = value
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def reg(self):
        return self.__reg
    
    @property
    def driver(self):
        return self.__driver
    
    @driver.setter
    def driver(self, driver: Driver):
        self.__driver = driver