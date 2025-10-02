import random

class TreeNodeStruct:
    def __init__(self, struct_value):
        self.node_value = struct_value
        self.left_sub = None
        self.right_sub = None

class BinSearchStructure:
    def __init__(self):
        self.top_element = None
    
    def insert_struct(self, value):
        if self.top_element is None:
            self.top_element = TreeNodeStruct(value)
        else:
            self._insert_struct_helper(self.top_element, value)
    
    def _insert_struct_helper(self, current_node, value):
        if value < current_node.node_value:
            if current_node.left_sub is None:
                current_node.left_sub = TreeNodeStruct(value)
            else:
                self._insert_struct_helper(current_node.left_sub, value)
        else:
            if current_node.right_sub is None:
                current_node.right_sub = TreeNodeStruct(value)
            else:
                self._insert_struct_helper(current_node.right_sub, value)
    
    def find_struct(self, value):
        if self.top_element is None:
            return None
        return self._find_struct_helper(self.top_element, value)
    
    def _find_struct_helper(self, current_node, value):
        if current_node is None or current_node.node_value == value:
            return current_node
        elif value < current_node.node_value:
            return self._find_struct_helper(current_node.left_sub, value)
        else:
            return self._find_struct_helper(current_node.right_sub, value)
    
    def print_tree(self):
        """Дополнительный метод для визуализации дерева (необязательный)"""
        self._print_tree_helper(self.top_element, 0)
    
    def _print_tree_helper(self, node, level):
        if node is not None:
            self._print_tree_helper(node.right_sub, level + 1)
            print(' ' * 4 * level + '->', node.node_value)
            self._print_tree_helper(node.left_sub, level + 1)

def main():
    # Создаем экземпляр класса BinSearchStructure
    tree = BinSearchStructure()
    
    # Генерируем 22 случайных числа от 2 до 42
    random_numbers = [random.randint(2, 42) for _ in range(22)]
    print("Случайные числа для вставки:", random_numbers)
    print()
    
    # Вставляем случайные числа в дерево
    for number in random_numbers:
        tree.insert_struct(number)
    
    # Выполняем поиск некоторых элементов
    search_values = [10, 15, 20, 25, 30, 35, 40]
    
    print("Результаты поиска:")
    for value in search_values:
        result = tree.find_struct(value)
        if result is not None:
            print(f"Значение {value} найдено в дереве")
        else:
            print(f"Значение {value} не найдено в дереве")
    
    # Дополнительно: поиск нескольких случайных чисел из вставленных
    print("\nПоиск случайных чисел из вставленных:")
    sample_numbers = random.sample(random_numbers, min(5, len(random_numbers)))
    for value in sample_numbers:
        result = tree.find_struct(value)
        if result is not None:
            print(f"Значение {value} найдено в дереве")
        else:
            print(f"Значение {value} не найдено в дереве")

if __name__ == "__main__":
    main()