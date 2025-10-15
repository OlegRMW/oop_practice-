class ThreadPool:
    
    _threads = []
    THREAD_MAX = 12
    
    def __new__(cls, *args):
        if len(cls._threads) >= cls.THREAD_MAX:
            raise RuntimeError('Достигнут лимит потоков!')
        else:
            obj = super().__new__(cls)
            cls._threads.append(obj)
            return obj
    
    def __init__(self, thread_id):
        self.thread = thread_id
    
    def __del__(self):
        for _ in self._threads:
            if _ == self:
                self._threads.remove(self)
                print(f'{self} удален', self._threads)
                
threads = [ThreadPool(f'Thread{i}') for i in range(12)]

try:
    t13 = ThreadPool('Thread13')
except RuntimeError as error:
    print('Ошибка:', error)

del threads[0], threads[1], threads[2], threads[3]

t13 = ThreadPool('Thread13')
t14 = ThreadPool('Thread14')
t15 = ThreadPool('Thread15')

print('Созданы потоки:', t13.thread, t14.thread, t15.thread)
