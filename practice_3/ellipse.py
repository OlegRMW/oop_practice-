import math 


#Переопределение метода __call__ при создании экземпляра 
class MyMeta(type):
    def __call__(cls, *args, **kwargs):
        arr = cls.__new__(cls, *args, **kwargs)
        obj = arr[0]
        axis = arr[1]
        cls.__init__(obj, axis)
        return obj

class Ellipse(metaclass=MyMeta):
    def __init__(self, major_axis: int):
        self.__major_axis = major_axis
        self.__minor_axis = 3

    def __repr__(self):
        return f'{self.__major_axis}'
    
    def calculate_area(self):
        return math.pi * self.__major_axis * 3
    
    def calculate_perimeter(self):
        return math.pi * (3 * (self.__major_axis + 3) - math.sqrt((3 * self.__major_axis + 3)*(self.__major_axis + 9)))
    
    # добавляю ввод параметра при создании объекта класса 
    def __new__(cls, *args):
        major_axis = int(input('Введите длину большей полуоси: \a'))
        print(f'Создан экземпляр класса {cls}')
        return [super().__new__(cls), major_axis]
            

 
