class Stationery:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color

    def apply(self):
        return "Применяется"

    def __str__(self):
        return f"{self.name} ({self.brand}, {self.color})"


class Pen(Stationery):
    def __init__(self, ink_type, name, brand, color):
        super().__init__(name, brand, color)
        self.ink_type = ink_type

    def apply(self):
        return "Пишет"

    def __str__(self):
        return f"{self.name} ({self.brand}, {self.color}, чернила: {self.ink_type})"


class Notebook(Stationery):
    def __init__(self, name, brand, color):
        super().__init__(name, brand, color)

    def apply(self):
        return "Заполняется"


class Ruler(Stationery):
    def __init__(self, name, brand, color):
        super().__init__(name, brand, color)

    def apply(self):
        return "Измеряет"


# Основная часть программы
if __name__ == "__main__":
    # создаём объекты
    pen1 = Pen("гелевые", "Ручка", "Parker", "синяя")
    pen2 = Pen("шариковые", "Ручка", "Pilot", "черная")
    notebook = Notebook("Тетрадь", "Erich Krause", "зеленая")
    ruler = Ruler("Линейка", "Maped", "прозрачная")

    # создаём список
    school = [pen1, pen2, notebook, ruler]

    # выводим содержимое
    print("Содержимое списка school:")
    for item in school:
        print(f"{item} — {item.apply()}")

    # удаляем объекты класса Pen
    school = [item for item in school if not isinstance(item, Pen)]

    # выводим оставшееся содержимое
    print("\nПосле удаления объектов класса Pen:")
    for item in school:
        print(f"{item} — {item.apply()}")
