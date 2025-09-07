import random
from order import Order
from driver import Driver 

class Dispatcher:
    def __init__(self, name, surname, patronymic):
        self.__id = random.randint(1000, 10000)
        self.__name = name 
        self.__surname = surname
        self.__patronymic = patronymic
        self.__assigned_orders = []
    
    def __repr__(self):
        return f"{self.surname} {self.name}  {self.patronymic}"
    
    def assign_passenger(self, order: Order, passenger_name, passenger_surname, passenger_patronymic):
        order.passenger_name = passenger_name
        order.passenger_surname = passenger_surname
        order.passenger_patronymic = passenger_patronymic
        print(f'Пассажир добавлен в заказ {order.id}')
    
    def create_order(self):
        order = Order()
        self.__assigned_orders.append(order)
        print(f'Диспетчер {self} создал заказ номер {order.id}')
        return order 
       
    def assign_order(self, order: Order, driver: Driver):
        driver.current_order = order 
        print(f'Водителю {driver} назначен заказ номер {order.id}')   
       
    @property
    def name(self):
        return self.__name
      
    @property
    def surname(self):
        return self.__surname
    
    @property
    def patronymic(self):
        return self.__patronymic
    
    @property
    def assigned_orders(self):
        return self.__assigned_orders
    

