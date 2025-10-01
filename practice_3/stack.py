class Stack:
    def __init__(self, validate_type=None):
        self._items = []  # защищенный атрибут для хранения элементов стека
        self._validate_type = validate_type  # тип для валидации элементов
    
    def push(self, item):
        """Добавляет элемент в стек с проверкой типа"""
        if self._validate_type is not None and not isinstance(item, self._validate_type):
            return False
        
        self._items.append(item)
        return True
    
    def pop(self):
        """Удаляет и возвращает верхний элемент стека"""
        if self.is_empty():
            return None
        return self._items.pop()
    
    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return len(self._items) == 0
    
    def size(self):
        """Возвращает количество элементов в стеке"""
        return len(self._items)
    
    def peek(self):
        """Возвращает верхний элемент стека без удаления"""
        if self.is_empty():
            return None
        return self._items[-1]
    
    def __str__(self):
        """Возвращает строковое представление стека"""
        return str(self._items)


# Создание экземпляра класса Stack с validate_type=int
stack = Stack(validate_type=int)

# Добавление элементов: 10, "20"(не добавится), 30, 40.5 (не добавится), 50
print("Добавление элементов в стек:")
print(stack.push(10))    # True
print(stack.push("20"))  # False
print(stack.push(30))    # True
print(stack.push(40.5))  # False
print(stack.push(50))    # True

print("\nТекущее состояние стека:")
print("Содержимое стека:", stack._items)  # [10, 30, 50]

# Вывод размера стека и верхнего элемента
print("\nИнформация о стеке:")
print("Размер стека:", stack.size())      # 3
print("Верхний элемент:", stack.peek())   # 50

# Вызов pop и вывод результата
popped = stack.pop()
print("\nОперация pop:")
print("Вытолкнут:", popped)               # 50

# Повторный вывод размера и верхнего элемента
print("\nИнформация о стеке после pop:")
print("Размер после pop:", stack.size())  # 2
print("Верхний элемент:", stack.peek())   # 30

# Дополнительная демонстрация работы методов
print("\n" + "="*50)
print("Дополнительная демонстрация:")

# Проверка на пустоту
print("Стек пуст?", stack.is_empty())

# Добавим еще несколько элементов
print("\nДобавляем дополнительные элементы:")
print(stack.push(60))    # True
print(stack.push("текст"))  # False
print(stack.push(70))    # True

print("Содержимое стека:", stack._items)  # [10, 30, 60, 70]

# Последовательное извлечение всех элементов
print("\nПоследовательное извлечение всех элементов:")
while not stack.is_empty():
    print(f"Извлечен: {stack.pop()}, осталось элементов: {stack.size()}")

# Попытка извлечения из пустого стека
print("\nПопытка извлечения из пустого стека:")
print("pop() из пустого стека:", stack.pop())  # None
print("peek() в пустом стеке:", stack.peek())  # None
print("Размер пустого стека:", stack.size())   # 0
print("Стек пуст?", stack.is_empty())          # True

# Демонстрация стека без проверки типов
print("\n" + "="*50)
print("Стек без проверки типов:")

any_stack = Stack()  # без validate_type
any_stack.push(10)
any_stack.push("текст")
any_stack.push(3.14)
any_stack.push([1, 2, 3])

print("Содержимое стека без проверки типов:", any_stack._items)