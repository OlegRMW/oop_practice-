from order import Order 
import time 

class Driver:
    def __init__(self, name, surname, current_order = ''):
        self.__name = name
        self.__surname = surname 
        self.__current_order = current_order 
        self.__complete_orders = [] 
        
    def __repr__(self):
        return f"{self.name} {self.surname}"
    
    def complete_order(self):
        try:
            travel_time = time.time() - self.current_order.date
            self.current_order.status = 'completed'
            self.current_order.travel_time = travel_time
            self.complete_orders.append(self.current_order)
            print(f'Водитель {self} завершил заказ номер {self.current_order.id} за {travel_time} секунд')
        except AttributeError:
            print(f'У водителя {self} нет активных заказов')
    
    @property    
    def name(self):
        return self.__name 
    
    @property
    def surname(self):
        return self.__surname 
    
    @property
    def complete_orders(self):
        return self.__complete_orders
    
    @complete_orders.setter
    def complete_orders(self, order):
        self.__complete_orders = order 
    
    @property
    def current_order(self):
        return self.__current_order
    
    @current_order.setter
    def current_order(self, order: Order):
        self.__current_order = order 
        
    
    