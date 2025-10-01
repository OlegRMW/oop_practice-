import ctypes

class Node:
    def __init__(self, value, pointer=None):
        self.__adress = id(self)
        self.__pointer = pointer
        self.__value = value
    
    def __repr__(self):
        return f'{self.__value}'
    
    @property 
    def adress(self):
        return self.__adress    
    
    @adress.setter
    def adress(self, adress):
        self.__adress = adress   
        
    @property 
    def value(self):
        return self.__value   
    
    @value.setter
    def value(self, value):
        self.__value = value   
    
    @property 
    def pointer(self):
        return self.__pointer  
    
    @pointer.setter
    def pointer(self, pointer):
        self.__pointer = pointer     

class OneList:
    def __init__(self):
        self.__start = None
        # self.__end = None
        
    def push(self, node: Node):
        if self.__start == None:
            self.__start = node
            print('Элемент добавлен в конец односвязного списка')
        
        current = self.__start 
        
        while current.pointer != None:
            current = current.pointer
        
        current.pointer = node 
        
        
    def pop(self):
        if self.__start == None:
            print('Список пуст')
            return  
            
        if self.__start.pointer == None:  
            del self.__start 
            self.__start = None  
            return  
        
        current = self.__start 
        
        while current.pointer != None:
            prev = current 
            current = current.pointer
                
        prev.pointer = None    
        del current
    
    def add_in_head(self, node: Node):
        if self.__start == None:
            self.__start = node
            print(f'Элемент добавлен в начало односвязного списка, адрес элемента {id(node)}')

    def add_on_position(self, node: Node, position: int):
        if self.__start == None:
            self.__start = id(node)
              
    @property
    def start(self):
        return self.__start
    
    
one_list = OneList()   
elem_1 = Node(1)
elem_2 = Node(2)
elem_3 = Node(3)
one_list.add_in_head(elem_1)
one_list.push(elem_2)
one_list.push(elem_3)
one_list.pop()

print(elem_2.pointer)




    
    