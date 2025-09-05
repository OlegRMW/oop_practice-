from car import Car 

class TaxiPark:

    def __init__(self):
        self.__drivers = []
        self.__cars = [] 

    def __repr__(self):
        # return f'Авто таксопарка: {self.__cars}'
        return f'{self.__dict__}'

    def add_car(car: Car):
        pass
    
    def add_driver():
        pass 
    
    def print_info():
        pass 
    
    def fire_driver():
        pass 
    
    @property
    def drivers(self):
        return self.__drivers
    
    @property
    def cars(self):
        return self.__cars 

taxi_park = TaxiPark()

print(taxi_park.drivers)
