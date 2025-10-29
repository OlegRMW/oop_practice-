class GasStaff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def giveRaise(self, amount=1000):
        """Увеличивает зарплату сотрудника"""
        self.salary += amount
        print(f"{self.name} получил(а) повышение. Новая зарплата: {self.salary} руб.")

    def work(self):
        """Общее сообщение для всех работников"""
        print(f"{self.name} работает на заправке.")

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', salary={self.salary})"


class Attendant(GasStaff):
    def __init__(self, name, salary=40000):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.name} заправляет автомобили.")


class ShopKeeper(GasStaff):
    def __init__(self, name, salary=35000):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.name} продаёт товары в магазине при АЗС.")


class WindowBot(Attendant):
    def __init__(self, name, salary=20000):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.name} моет лобовые стёкла автомобилей.")


# Основная часть программы
if __name__ == "__main__":
    # Создаём объекты
    attendant = Attendant("Иван")
    shopkeeper = ShopKeeper("Ольга")
    windowy = WindowBot("Робот-2000")

    # (k) Вызываем методы для windowy
    print("\nРабота WindowBot:")
    windowy.work()
    windowy.giveRaise()

    # (l) Вызываем метод work у всех сотрудников
    print("\nРабота всей команды:")
    staff_list = [attendant, shopkeeper, windowy]
    for worker in staff_list:
        worker.work()
