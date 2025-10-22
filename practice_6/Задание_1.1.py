class Spaceship:
    def __init__(self):
        self.__speed = 0
        self.__distance = 0
        self.__max_speed = 30000
        self.__passengers = []
        self.__capacity = 5
        self.__empty_seats = self.__capacity
        self.__seats_occupied = 0
        self.__fuel_tank = 1000
        self.__fuel = 0
        self.__engine_oil_capacity = 10
        self.__engine_oil = 0
        self.__luggage_spaces = 10
        self.__luggage = []

    def get_speed(self): return self.__speed
    def get_distance(self): return self.__distance
    def get_max_speed(self): return self.__max_speed
    def get_passengers(self): return self.__passengers
    def get_capacity(self): return self.__capacity
    def get_empty_seats(self): return self.__empty_seats
    def get_seats_occupied(self): return self.__seats_occupied
    def get_fuel_tank(self): return self.__fuel_tank
    def get_fuel(self): return self.__fuel
    def get_engine_oil_capacity(self): return self.__engine_oil_capacity
    def get_engine_oil(self): return self.__engine_oil
    def get_luggage_spaces(self): return self.__luggage_spaces
    def get_luggage(self): return self.__luggage

    def set_speed(self, value):
        if 0 <= value <= self.__max_speed:
            self.__speed = value
        else:
            raise ValueError("Недопустимая скорость!")

    def set_distance(self, value):
        if value >= 0:
            self.__distance = value
        else:
            raise ValueError("Расстояние не может быть отрицательным!")

    def set_passengers(self, passengers):
        if len(passengers) <= self.__capacity:
            self.__passengers = passengers
            self.__seats_occupied = len(passengers)
            self.__empty_seats = self.__capacity - len(passengers)
        else:
            raise ValueError("Превышена вместимость пассажиров!")

    def set_empty_seats(self, value):
        if 0 <= value <= self.__capacity:
            self.__empty_seats = value
        else:
            raise ValueError("Некорректное число свободных мест!")

    def set_seats_occupied(self, value):
        if 0 <= value <= self.__capacity:
            self.__seats_occupied = value
        else:
            raise ValueError("Некорректное число занятых мест!")

    def set_fuel(self, value):
        if 0 <= value <= self.__fuel_tank:
            self.__fuel = value
        else:
            raise ValueError("Недопустимый уровень топлива!")

    def set_engine_oil(self, value):
        if 0 <= value <= self.__engine_oil_capacity:
            self.__engine_oil = value
        else:
            raise ValueError("Недопустимое количество масла!")

    def set_luggage(self, luggage):
        if len(luggage) <= self.__luggage_spaces:
            self.__luggage = luggage
        else:
            raise ValueError("Превышено количество багажных мест!")

    # Геттеры, сеттеры 
    speed = property(get_speed, set_speed)
    distance = property(get_distance, set_distance)
    passengers = property(get_passengers, set_passengers)
    empty_seats = property(get_empty_seats, set_empty_seats)
    seats_occupied = property(get_seats_occupied, set_seats_occupied)
    fuel = property(get_fuel, set_fuel)
    engine_oil = property(get_engine_oil, set_engine_oil)
    luggage = property(get_luggage, set_luggage)

    # Только геттеры 
    max_speed = property(get_max_speed)
    capacity = property(get_capacity)
    fuel_tank = property(get_fuel_tank)
    engine_oil_capacity = property(get_engine_oil_capacity)
    luggage_spaces = property(get_luggage_spaces)


    def show_info(self):
        print(f"Скорость: {self.__speed}")
        print(f"Пройдено: {self.__distance}")
        print(f"Пассажиры: {self.__passengers}")
        print(f"Свободно мест: {self.__empty_seats}")
        print(f"Занято мест: {self.__seats_occupied}")
        print(f"Топливо: {self.__fuel}/{self.__fuel_tank}")
        print(f"Масло: {self.__engine_oil}/{self.__engine_oil_capacity}")
        print(f"Багаж: {self.__luggage}")


myspace1 = Spaceship()
myspace1.speed = 12000
myspace1.fuel = 600
myspace1.passengers = ["Илон", "Марсель", "Люси"]
myspace1.luggage = ["робот", "инструменты"]

myspace1.show_info()
