class HullSeal:
    def __init__(self):
        self.is_sealed = False

    def seal_hull(self):
        self.is_sealed = True
        print("Все люки и клапаны закрыты.")

    def unseal_hull(self):
        self.is_sealed = False
        print("Все люки и клапаны открыты.")

    def check_pressure(self):
        if self.is_sealed:
            print("Герметичность корпуса в норме.")
        else:
            print("ВНИМАНИЕ: корпус негерметичен!")

seal = HullSeal()

seal.seal_hull()
seal.check_pressure()
seal.unseal_hull()
