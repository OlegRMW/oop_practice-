class Device:
    def __init__(self, brand, model, battery_level):
        self.__brand = brand
        self.__model = model
        self.__battery_level = battery_level

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def battery_level(self):
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        self.__battery_level = value

    def charge(self, percent):
        self.battery_level += percent

    def get_brand_initial(self):
        return self.__brand[0].upper()

    def __repr__(self):
        return f"Device(brand='{self.__brand}', model='{self.__model}', battery={self.__battery_level}%)"


class Smartphone(Device):
    def __init__(self, brand, model, battery_level):
        super().__init__(brand, model, battery_level)

    def charge(self, percent):
        extra = 5
        super().charge(percent + extra)


device = Device("Lenovo", "Tab M10", 45)
smartphone = Smartphone("Samsung", "Galaxy S23", 30)

device.charge(10)
smartphone.charge(10)

print(device)
print(smartphone)

print("Первая буква бренда Device:", device.get_brand_initial())
print("Первая буква бренда Smartphone:", smartphone.get_brand_initial())
