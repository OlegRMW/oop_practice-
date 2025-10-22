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

    # ========== speed ==========
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= self.__max_speed:
            self.__speed = value
        else:
            raise ValueError("Недопустимая скорость")

    # ========== distance ==========
    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        if value >= 0:
            self.__distance = value
        else:
            raise ValueError("Расстояние не может быть отрицательным")

    # ========== max_speed (только чтение) ==========
    @property
    def max_speed(self):
        return self.__max_speed

    # ========== passengers ==========
    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        if len(value) <= self.__capacity:
            self.__passengers = value
            self.__seats_occupied = len(value)
            self.__empty_seats = self.__capacity - len(value)
        else:
            raise ValueError("Превышена вместимость пассажиров")

    # ========== capacity (только чтение) ==========
    @property
    def capacity(self):
        return self.__capacity

    # ========== empty_seats ==========
    @property
    def empty_seats(self):
        return self.__empty_seats

    @empty_seats.setter
    def empty_seats(self, value):
        if 0 <= value <= self.__capacity:
            self.__empty_seats = value
        else:
            raise ValueError("Недопустимое количество свободных мест")

    # ========== seats_occupied ==========
    @property
    def seats_occupied(self):
        return self.__seats_occupied

    @seats_occupied.setter
    def seats_occupied(self, value):
        if 0 <= value <= self.__capacity:
            self.__seats_occupied = value
        else:
            raise ValueError("Недопустимое количество занятых мест")

    # ========== fuel_tank (только чтение) ==========
    @property
    def fuel_tank(self):
        return self.__fuel_tank

    # ========== fuel ==========
    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if 0 <= value <= self.__fuel_tank:
            self.__fuel = value
        else:
            raise ValueError("Недопустимое количество топлива")

    # ========== engine_oil_capacity (только чтение) ==========
    @property
    def engine_oil_capacity(self):
        return self.__engine_oil_capacity

    # ========== engine_oil ==========
    @property
    def engine_oil(self):
        return self.__engine_oil

    @engine_oil.setter
    def engine_oil(self, value):
        if 0 <= value <= self.__engine_oil_capacity:
            self.__engine_oil = value
        else:
            raise ValueError("Недопустимое количество масла")

    # ========== luggage_spaces (только чтение) ==========
    @property
    def luggage_spaces(self):
        return self.__luggage_spaces

    # ========== luggage ==========
    @property
    def luggage(self):
        return self.__luggage

    @luggage.setter
    def luggage(self, value):
        if len(value) <= self.__luggage_spaces:
            self.__luggage = value
        else:
            raise ValueError("Превышено количество багажных мест")

    def show_info(self):
        print(f"Скорость: {self.__speed}/{self.__max_speed}")
        print(f"Пройденное расстояние: {self.__distance}")
        print(f"Пассажиры: {self.__passengers}")
        print(f"Вместимость: {self.__capacity}")
        print(f"Свободные места: {self.__empty_seats}")
        print(f"Занятые места: {self.__seats_occupied}")
        print(f"Топливо: {self.__fuel}/{self.__fuel_tank}")
        print(f"Масло: {self.__engine_oil}/{self.__engine_oil_capacity}")
        print(f"Багаж: {self.__luggage} ({len(self.__luggage)}/{self.__luggage_spaces})")

