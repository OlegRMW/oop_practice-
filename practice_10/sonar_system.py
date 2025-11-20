class SonarSystem:
    def scan_area(self):
        return "Сканирование дна начато."

    def detect_object(self):
        return "Объект обнаружен на глубине 15 м."

    def map_seabed(self):
        return "Карта дна сгенерирована."



sonar = SonarSystem()

data = sonar.scan_area()
print("Найден объект:", sonar.detect_object())
print("Карта дна:", sonar.map_seabed())
