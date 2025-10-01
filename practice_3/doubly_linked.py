class Node:
    def __init__(self, data):
        self._val = data
        self._link_f = None  # Ссылка на следующий узел (forward)
        self._link_b = None  # Ссылка на предыдущий узел (backward)


class DoublyLinkedList:
    def __init__(self):
        self._first_item = None
        self._last_item = None
    
    def display(self):
        # Прямой порядок
        current = self._first_item
        forward_list = []
        while current is not None:
            forward_list.append(str(current._val))
            current = current._link_f
        
        # Обратный порядок
        current = self._last_item
        backward_list = []
        while current is not None:
            backward_list.append(str(current._val))
            current = current._link_b
        
        if not forward_list:
            print("Нет данных")
        else:
            print("Элементы (прямой порядок):", " <-> ".join(forward_list))
            print("Элементы (обратный порядок):", " <-> ".join(backward_list))
    
    def insert(self, value):
        new_node = Node(value)
        
        # Если список пуст
        if self._first_item is None:
            self._first_item = new_node
            self._last_item = new_node
            return
        
        # Находим узел с максимальным значением
        max_node = self._first_item
        current = self._first_item._link_f
        
        while current is not None:
            if current._val > max_node._val:
                max_node = current
            current = current._link_f
        
        # Вставляем перед max_node
        if max_node._link_b is None:  # max_node - первый элемент
            new_node._link_f = max_node
            max_node._link_b = new_node
            self._first_item = new_node
        else:  # max_node не первый элемент
            prev_node = max_node._link_b
            new_node._link_f = max_node
            new_node._link_b = prev_node
            prev_node._link_f = new_node
            max_node._link_b = new_node
    
    def delete(self, value):
        current = self._first_item
        
        while current is not None:
            next_node = current._link_f
            
            if current._val == value:
                # Удаляем текущий узел
                if current._link_b is None:  # Первый элемент
                    self._first_item = current._link_f
                    if self._first_item is not None:
                        self._first_item._link_b = None
                    else:
                        self._last_item = None
                elif current._link_f is None:  # Последний элемент
                    self._last_item = current._link_b
                    self._last_item._link_f = None
                else:  # Элемент в середине
                    prev_node = current._link_b
                    next_node = current._link_f
                    prev_node._link_f = next_node
                    next_node._link_b = prev_node
            
            current = next_node


# Создание экземпляра класса DoublyLinkedList
dll = DoublyLinkedList()

# Вставка узлов: 5, 15, 10
dll.insert(5)
dll.insert(15)
dll.insert(10)

print("Initial Doubly Linked List:")
dll.display()

# Вставка 12 (перед 15 - максимальным)
dll.insert(12)

print("After inserting 12 before max:")
dll.display()

# Удаление всех вхождений 10
dll.delete(10)

print("After deleting all 10s:")
dll.display()