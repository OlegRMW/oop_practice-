class Queue:
    def __init__(self, reverse_dequeue=False):
        self._pipe = []  # защищенный атрибут для хранения элементов
        self._reverse_dequeue = reverse_dequeue  # флаг направления извлечения
    
    def enqueue(self, item):
        """Добавляет элемент в конец очереди"""
        self._pipe.append(item)
    
    def dequeue(self):
        """Удаляет и возвращает элемент из очереди"""
        if self.is_empty():
            raise IndexError("Пусто")
        
        if self._reverse_dequeue:
            # Удаляем и возвращаем последний элемент
            return self._pipe.pop()
        else:
            # Удаляем и возвращаем первый элемент
            return self._pipe.pop(0)
    
    def is_empty(self):
        """Проверяет, пуста ли очередь"""
        return len(self._pipe) == 0
    
    def __str__(self):
        """Возвращает строковое представление очереди"""
        return str(self._pipe)


# Создание экземпляра класса Queue с reverse_dequeue=True
queue = Queue(reverse_dequeue=True)

# Добавление элементов: 10, 20, 30
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Вывод текущего состояния очереди
print("Current Queue:", queue._pipe)  # [10, 20, 30]

# Вызов dequeue - должен вернуться 30 (последний)
try:
    dequeued_item = queue.dequeue()  # 30
    print("Dequeued item:", dequeued_item)
except IndexError as e:
    print("Error:", e)

# Вывод обновленного состояния очереди
print("Updated Queue:", queue._pipe)  # [10, 20]

# Демонстрация дополнительных операций
print("\n--- Дополнительная демонстрация ---")

# Проверка на пустоту
print("Очередь пуста?", queue.is_empty())

# Еще одно извлечение
try:
    dequeued_item2 = queue.dequeue()  # 20 (теперь последний)
    print("Второй извлеченный элемент:", dequeued_item2)
    print("Очередь после второго извлечения:", queue._pipe)  # [10]
except IndexError as e:
    print("Error:", e)

# Создадим обычную очередь (FIFO) для сравнения
print("\n--- Сравнение с обычной очередью (FIFO) ---")
normal_queue = Queue(reverse_dequeue=False)  # обычное поведение
normal_queue.enqueue(10)
normal_queue.enqueue(20)
normal_queue.enqueue(30)
print("Обычная очередь:", normal_queue._pipe)  # [10, 20, 30]

try:
    normal_dequeued = normal_queue.dequeue()  # 10 (первый)
    print("Извлечен из обычной очереди:", normal_dequeued)
    print("Обычная очередь после извлечения:", normal_queue._pipe)  # [20, 30]
except IndexError as e:
    print("Error:", e)