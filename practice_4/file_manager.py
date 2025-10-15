class FileManager:
    __manager = None 
    
    def __new__(cls, *args):
        if cls.__manager is None: 
            __manager = super().__new__(cls)
            return __manager
        else:
            return __manager
    
    def __init__(self, path, mode, buffered):
        self.__path = path
        self.__mode = mode 
        self.__buffered = buffered
        
    def open(self):
        print(f'Открытие файла {self.__path} в режиме {self.__mode} (буферизация: {self.__buffered})') 
        
    def __del__(self):
        print('Файл закрыт')

    def read(self):
        print('Данные прочитаны')
        
    def write(self, data):
        print(f'Данные {data} записаны')
    
    @property 
    def path(self):
        return self.__path
    
    @property 
    def mode(self):
        return self.__mode
    
    @property 
    def buffered(self):
        return self.__buffered
    
    
fm1 = FileManager('data.txt', 'r', True)
fm2 = FileManager('log.txt', 'w', False)

fm1.open()
fm2.write('Hello')


print('Mode:', fm1.mode)