from hull_seal import HullSeal
from sonar_system import SonarSystem

class Submarine:
    def __init__(self, depth_rating=500, ballast_type="water"):
        self._depth_rating = depth_rating
        self._ballast_type = ballast_type
        self.mass = 1000   
        self.power = 5000  
    
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
        return f"Субмарина погружается на {self._depth_rating} метров, используя {self._ballast_type}"
    
    def navigate_underwater(self):
        return "Навигация под водой, ипользуя гидролокатор и перископ"


class Hovercraft(Submarine):
    def __init__(self, skirt_material="rubber", engine_power=1000, terrain_type="mixed"):
        super().__init__() 
        self._skirt_material = skirt_material
        self._engine_power = engine_power
        self._terrain_type = terrain_type
        self.mass = 10     
        self.power = 1000  
    
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
            raise ValueError("Мощность двигателя не может быть отрицательной!")
    
    @property
    def terrain_type(self):
        return self._terrain_type
    
    @terrain_type.setter
    def terrain_type(self, value):
        self._terrain_type = value
    
    def inflate_skirt(self):
        return f"Надувание {self._skirt_material} юбки для {self._terrain_type} местности"
    
    def navigate_underwater(self):
        return "Судно на воздушной подушке не может двигаться под водой - сдуйте юбку!"
    
    def deflate(self):
        return "Сдувание юбки и подготовка к путешествию по суше"

class AmphibiousVehicle(Submarine, HullSeal):
    def __init__(self, wheel_type="all-terrain", propeller_count=2, land_speed=80, water_speed=20):
        super().__init__()  
        HullSeal.__init__(self)  
        self._wheel_type = wheel_type
        self._propeller_count = propeller_count
        self._land_speed = land_speed
        self._water_speed = water_speed
        self.mass = 5      
        self.power = 300   
            
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
            raise ValueError("Количество пропеллеров не может быть отрицательным!")
    
    @property
    def land_speed(self):
        return self._land_speed
    
    @land_speed.setter
    def land_speed(self, value):
        if value >= 0:
            self._land_speed = value
        else:
            raise ValueError("Скорость не может быть отрицательна!")
    
    @property
    def water_speed(self):
        return self._water_speed
    
    @water_speed.setter
    def water_speed(self, value):
        if value >= 0:
            self._water_speed = value
        else:
            raise ValueError("Скорость не может быть отрицательна!")
    
    def switch_mode(self):
        print("Режим переключён: вода → суша")

class AmphibiousAcceleration:

    ETA_LAND = 0.80
    ETA_WATER = 0.70

    K_LAND_SEGMENTS = [
        (0, 10, 0.22),
        (10, 20, 0.30),
        (20, 30, 0.38),
        (30, 40, 0.46),
        (40, 50, 0.54),
    ]

    K_WATER = 0.18

    def _segment_time(self, dv, k, eta):
        m = self.mass * 1000        
        P = self.power * 735         
        return k * dv * m / (P * eta)

    def accel_land(self):
        total = 0
        for v1, v2, k in self.K_LAND_SEGMENTS:
            dv = v2 - v1
            total += self._segment_time(dv, k, self.ETA_LAND)
        return total

    def accel_water(self):
        return self._segment_time(30, self.K_WATER, self.ETA_WATER)


class AmphibiousCraft(AmphibiousAcceleration, SonarSystem, Hovercraft, AmphibiousVehicle):

    def __init__(self, depth_rating=300, ballast_type="water",
                 skirt_material="neoprene", engine_power=1500, terrain_type="amphibious",
                 wheel_type="all-terrain", propeller_count=4, land_speed=60, water_speed=25):

        Hovercraft.__init__(self, skirt_material, engine_power, terrain_type)
        AmphibiousVehicle.__init__(self, wheel_type, propeller_count, land_speed, water_speed)
        SonarSystem.__init__(self)  

        self._depth_rating = depth_rating
        self._ballast_type = ballast_type
        
        self.mass = 1000 + 10 + 5  
        self.power = 5000 + 1000 + 300  

    def run(self):
        actions = []

        actions.append(self.seal_hull())
        actions.append(self.check_pressure())
        actions.append(self.unseal_hull())

        actions.append(self.scan_area())
        actions.append(self.detect_object())
        actions.append(self.map_seabed())

        actions.append(self.submerge())
        actions.append(self.inflate_skirt())
        actions.append(self.switch_mode())
        actions.append(self.navigate_underwater())

        actions.append(
            f"Depth rating: {self.depth_rating} m, "
            f"Skirt material: {self.skirt_material}, "
            f"Wheel type: {self.wheel_type}"
        )

        return actions

craft = AmphibiousCraft()
print(craft.accel_land())
print(craft.accel_water())