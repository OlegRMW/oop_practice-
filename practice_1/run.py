from taxi_park import TaxiPark
from driver import Driver 
from order import Order 
from car import Car
from dispatcher import Dispatcher
import time 

def progress_bar(total_seconds: int):
    steps = 20  
    interval = total_seconds / steps  

    print("Везём пассажира:", end=" ")
    
    for _ in range(steps):
        time.sleep(interval)  
        print("-", end="", flush=True)  
        
    print(" Готово!")


taxi_park = TaxiPark()
driver_1 = Driver('Max', 'Polls')
driver_2 = Driver('Alex', 'Maison')
car_1 = Car('Volvo XC60', 'ПР091Н', driver_1)
car_2 = Car('Skoda Rapid', 'РК089Н', driver_2)
taxi_park.add_driver(driver_1)
taxi_park.add_driver(driver_2)
taxi_park.add_car(car_1)
taxi_park.add_car(car_2)
car_1.assign_driver(driver_1)
car_2.assign_driver(driver_2)
dispatcher = Dispatcher('Oleg', 'Zagudaev', 'Denisovich')
order = dispatcher.create_order()
dispatcher.assign_passenger(order, 'Bob', 'Dylan', '---')
dispatcher.assign_order(order, driver_1)
progress_bar(5)
driver_1.complete_order()
print(taxi_park)
print(driver_1.complete_orders)

driver_2.complete_order()

car_1.increase_mileage(200)