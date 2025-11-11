class Submarine:
    def __init__(self, depth_rating=500, ballast_type="water", **kwargs):
        print("Start Submarine.__init__")
        super().__init__(**kwargs)
        self._depth_rating = depth_rating
        self._ballast_type = ballast_type
        print("End Submarine.__init__")
    
    @property
    def depth_rating(self):
        return self._depth_rating
    
    @depth_rating.setter
    def depth_rating(self, value):
        if value > 0:
            self._depth_rating = value
        else:
            raise ValueError("Depth rating must be positive")
    
    @property
    def ballast_type(self):
        return self._ballast_type
    
    @ballast_type.setter
    def ballast_type(self, value):
        self._ballast_type = value
    
    def submerge(self):
        return f"Submarine submerging to {self._depth_rating} meters using {self._ballast_type} ballast"
    
    def navigate_underwater(self):
        return "Navigating underwater with sonar and periscope"


class Hovercraft:
    def __init__(self, skirt_material="rubber", engine_power=1000, terrain_type="mixed", **kwargs):
        print("Start Hovercraft.__init__")
        super().__init__(**kwargs)
        self._skirt_material = skirt_material
        self._engine_power = engine_power
        self._terrain_type = terrain_type
        print("End Hovercraft.__init__")
    
    @property
    def skirt_material(self):
        return self._skirt_material
    
    @skirt_material.setter
    def skirt_material(self, value):
        self._skirt_material = value
    
    @property
    def engine_power(self):
        return self._engine_power
    
    @engine_power.setter
    def engine_power(self, value):
        if value > 0:
            self._engine_power = value
        else:
            raise ValueError("Engine power must be positive")
    
    @property
    def terrain_type(self):
        return self._terrain_type
    
    @terrain_type.setter
    def terrain_type(self, value):
        self._terrain_type = value
    
    def inflate_skirt(self):
        return f"Inflating {self._skirt_material} skirt for {self._terrain_type} terrain"
    
    def navigate_underwater(self):
        return "Hovercraft cannot navigate underwater - deflating skirt!"
    
    def deflate(self):
        return "Deflating skirt and preparing for land travel"


class AmphibiousVehicle:
    def __init__(self, wheel_type="all-terrain", propeller_count=2, land_speed=80, water_speed=20, **kwargs):
        print("Start AmphibiousVehicle.__init__")
        super().__init__(**kwargs)
        self._wheel_type = wheel_type
        self._propeller_count = propeller_count
        self._land_speed = land_speed
        self._water_speed = water_speed
        print("End AmphibiousVehicle.__init__")
    
    @property
    def wheel_type(self):
        return self._wheel_type
    
    @wheel_type.setter
    def wheel_type(self, value):
        self._wheel_type = value
    
    @property
    def propeller_count(self):
        return self._propeller_count
    
    @propeller_count.setter
    def propeller_count(self, value):
        if value >= 0:
            self._propeller_count = value
        else:
            raise ValueError("Propeller count cannot be negative")
    
    @property
    def land_speed(self):
        return self._land_speed
    
    @land_speed.setter
    def land_speed(self, value):
        if value >= 0:
            self._land_speed = value
        else:
            raise ValueError("Speed cannot be negative")
    
    @property
    def water_speed(self):
        return self._water_speed
    
    @water_speed.setter
    def water_speed(self, value):
        if value >= 0:
            self._water_speed = value
        else:
            raise ValueError("Speed cannot be negative")
    
    def switch_mode(self):
        return f"Switching mode: {self._wheel_type} wheels for land, {self._propeller_count} propellers for water"


class AmphibiousCraft(Submarine, Hovercraft, AmphibiousVehicle):
    def __init__(self, depth_rating=300, ballast_type="water", 
                 skirt_material="neoprene", engine_power=1500, terrain_type="amphibious",
                 wheel_type="amphibious", propeller_count=4, land_speed=60, water_speed=25):
        print("Start AmphibiousCraft.__init__")
        super().__init__(
            depth_rating=depth_rating,
            ballast_type=ballast_type,
            skirt_material=skirt_material,
            engine_power=engine_power,
            terrain_type=terrain_type,
            wheel_type=wheel_type,
            propeller_count=propeller_count,
            land_speed=land_speed,
            water_speed=water_speed
        )
        print("End AmphibiousCraft.__init__")
    
    def traverse(self):
        actions = []
        actions.append(self.submerge())
        actions.append(self.inflate_skirt())
        actions.append(self.switch_mode())
        actions.append(self.navigate_underwater())
        return actions
    
    def get_status(self):
        return {
            'depth_rating': self.depth_rating,
            'ballast_type': self.ballast_type,
            'skirt_material': self.skirt_material,
            'engine_power': self.engine_power,
            'terrain_type': self.terrain_type,
            'wheel_type': self.wheel_type,
            'propeller_count': self.propeller_count,
            'land_speed': self.land_speed,
            'water_speed': self.water_speed
        }


if __name__ == "__main__":
    
    craft = AmphibiousCraft()
    
    print("\n=== АМФИБИЙНЫЙ ТРАНСПОРТ ===")
    print("\nТекущее состояние:")
    status = craft.get_status()
    for key, value in status.items():
        print(f"{key}: {value}")
    
    print("\n=== ТЕСТИРОВАНИЕ МЕТОДОВ ===")
    
    print("\n1. Погружение:", craft.submerge())
    print("2. Надувание юбки:", craft.inflate_skirt())
    print("3. Переключение режима:", craft.switch_mode())
    print("4. Подводная навигация:", craft.navigate_underwater())
    print("5. Сдувание юбки:", craft.deflate())
    
    print("\n=== ПОЛНАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ TRAVERSE ===")
    actions = craft.traverse()
    for i, action in enumerate(actions, 1):
        print(f"{i}. {action}")
    
    print("\n=== ИЗМЕНЕНИЕ СВОЙСТВ ===")

    craft.depth_rating = 400
    craft.engine_power = 2000
    craft.land_speed = 70
    
    print(f"Новый рейтинг глубины: {craft.depth_rating}")
    print(f"Новая мощность двигателя: {craft.engine_power}")
    print(f"Новая скорость по земле: {craft.land_speed}")
    
    print(f"\nMRO (Method Resolution Order): {AmphibiousCraft.__mro__}")