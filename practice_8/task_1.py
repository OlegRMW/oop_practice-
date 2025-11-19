class Device:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def charge(self, percent):
        self.battery_level += percent
        if self.battery_level > 100:
            self.battery_level = 100

    def get_brand_initial(self):
        return self.brand[0].upper()

    def __repr__(self):
        return f"Device(brand='{self.brand}', model='{self.model}', battery={self.battery_level}%)"


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

