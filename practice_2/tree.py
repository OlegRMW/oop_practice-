from plant import Plant

class Tree(Plant):
    def __init__(self, height_rate, time, area, water_rate):
        self.__height_rate = height_rate
        self.__time = time
        self.__area = area
        self.__water_rate = water_rate

    @property
    def height_rate(self):
        return self.__height_rate

    @property
    def time(self):
        return self.__time

    @property
    def area(self):
        return self.__area

    @property
    def water_rate(self):
        return self.__water_rate

    def calculate_growth(self):
        return self.__height_rate * self.__time

    def calculate_water_needs(self):
        return self.__area * self.__water_rate
    
tree = Tree(2, 5, 10, 3)
print("Скорость роста дерева:", tree.height_rate)
print("Рост:", tree.calculate_growth())
print("Потребность в воде:", tree.calculate_water_needs())