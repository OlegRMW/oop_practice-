from order import Order 

class Driver:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname 
        self.__order_list = [] 
        
    def __repr__(self):
        return f"{self.name} {self.surname} - выполненные заказы: {self.__order_list}"
    
    def complete_order(order: Order):
        pass 
    
    @property    
    def name(self):
        return self.__name 
    
    @property
    def surname(self):
        return self.__surname 