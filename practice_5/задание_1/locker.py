class Locker:
    NumList: list[str] = [
        f"Камера_{i}" for i in range(1, 15)  
    ]
    MasList: list[str] = [
        "Велосипед", "Чемодан", "Инструменты", "Спортинвентарь"
    ]

    def __init__(self) -> None:
        self.storage = {
            num: None for num in Locker.NumList
        }

    def __repr__(self):
        return f"Locker({len(self.NumList)} камер, {len(self.MasList)} типов содержимого)"

