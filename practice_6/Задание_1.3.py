from accessify import private

class Spaceship3:
    # @private
    # def __max_speed(): return 30000
    # @private
    # def __capacity(): return 5
    # @private
    # def __fuel_tank(): return 1000
    # @private
    # def __engine_oil_capacity(): return 10
    # @private
    # def __luggage_spaces(): return 10

    def __init__(self):
        self.__speed = 0
        self.__fuel = 0
        self.__passengers = []
        self.__luggage = []
        self.__max_speed = 30000
        self.__capacity = 5
        self.__fuel_tank = 1000
        self.__engine_oil_capacity = 10
        self.__luggage_spaces = 10

    @private
    def check_speed(self, value):
        if not 0 <= value <= self.__max_speed:
            raise ValueError("Недопустимая скорость!")

    @private
    def check_fuel(self, value):
        if not 0 <= value <= self.__fuel_tank:
            raise ValueError("Недопустимый уровень топлива!")

    def get_speed(self): return self.__speed
    def set_speed(self, value):
        self.check_speed(value)
        self.__speed = value

    def get_fuel(self): return self.__fuel
    def set_fuel(self, value):
        self.check_fuel(value)
        self.__fuel = value

    def show_info(self):
        print(f"Скорость: {self.__speed}, Топливо: {self.__fuel}")


myspace3 = Spaceship3()
myspace3.set_speed(15000)
myspace3.set_fuel(800)
myspace3.show_info()

try:
    print(myspace3.__max_speed)
except Exception as e:
    print("Ошибка доступа:", e)
