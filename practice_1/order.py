import time 
import random

class Order:
    
    def __init__(self):
        self.__id = random.randint(1000, 10000)
        self.__date = time.ctime()
        self.__status = 'active'
        self.__passenger_name = ''
        self.__passenger_surname = ''
        self.__passenger_patronymic = ''
        
    def __repr__(self):
        return f"Информация о заказе: {self.__dict__}"

    @property
    def id(self):
        return self.__id
    
    @property
    def date(self):
        return self.__date
    
    @property
    def status(self):
        return self.__status 

    @property
    def passenger_name(self):
        return self.__passenger_name 
    
    @passenger_name.setter
    def passenger_name(self, name):
        self.__passenger_name = name
    
    @property
    def passenger_surname(self):
        return self.__passenger_surname 
    
    @passenger_surname.setter
    def passenger_surname(self, surname):
        self.__passenger_surname = surname
    
    @property
    def passenger_patronymic(self):
        return self.__passenger_patronymic
    
    @passenger_patronymic.setter
    def passenger_patronymic(self, patronymic):
        self.__passenger__patronymic = patronymic