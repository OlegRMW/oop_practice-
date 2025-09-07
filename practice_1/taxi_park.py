from car import Car 
from driver import Driver 

class TaxiPark:

    def __init__(self):
        self.__drivers = []
        self.__cars = [] 

    def __repr__(self):
        return f'Информация о таксопарке:\n  Водители: {self.drivers}\n  Автомобили: {self.cars}'

    def add_car(self, car: Car):
        self.cars.append(car)
        print(f'Авто {car} успешно добавлено в таксопарк!')
    
    def add_driver(self,  driver: Driver):
        self.drivers.append({'name': driver.name, 'surname': driver.surname})
        print(f'Водитель {driver} успешно добавлен в таксопарк!')
    
    def fire_driver(self, id: Driver):
        self.drivers.pop(id)
    
    @property
    def drivers(self):
        return self.__drivers
    
    @property
    def cars(self):
        return self.__cars 

