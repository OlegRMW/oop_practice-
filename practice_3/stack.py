class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top  
        self.top = new_node      
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        data = self.top.data      
        self.top = self.top.next  
        self._size -= 1
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
    
