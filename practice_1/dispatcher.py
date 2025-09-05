import random
from order import Order
from driver import Driver 

class Dispatcher:
    def __init__(self, name, surname, patronymic):
        self.__id = random.randint(1000, 10000)
        self.__name = name 
        self.__patronymic = patronymic
        self.__assigned_orders = []
    
    def assign_passenger(self, order: Order, passenger_name, passenger_surname, passenger_patronymic):
        order.passenger_name = passenger_name
        order.passenger_surname = passenger_surname
        order.passenger_patronymic = passenger_patronymic
        print('Пассажир добавлен в заказ')
        
    def assign_driver(order: Order, driver: Driver):
        pass 
    
    def assign_order(self):
        order = Order()
        self.__assigned_orders.append(order)
        print('Заказ создан и добавлен в список назначенных')
        return order 
    
    @property
    def assigned_orders(self):
        return self.__assigned_orders
    
dispatcher = Dispatcher('Oleg', 'Zagudaev', 'Denisovich')
order = dispatcher.assign_order()
dispatcher.assign_passenger(order, 'Alex', 'Maison', 'Popa')
print(dispatcher.assigned_orders)
