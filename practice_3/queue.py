class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self, reverse_dequeue=False):
        if self.is_empty():
            raise IndexError("Пусто")

        # (1) Удаляем первый элемент
        if not reverse_dequeue:
            value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return value

        # (2) Удаляем последний элемент
        else:
            # Если только один элемент
            if self.front == self.rear:
                value = self.front.value
                self.front = self.rear = None
                return value

            # Иначе ищем предпоследний элемент
            current = self.front
            while current.next != self.rear:
                current = current.next

            value = self.rear.value
            current.next = None
            self.rear = current
            return value


