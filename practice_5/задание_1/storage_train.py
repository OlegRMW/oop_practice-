import random
from locker import Locker


class StorageTrain:
    def __init__(self) -> None:
        self.train: list[Locker] = [Locker() for _ in range(56)]

    def shuffle(self) -> None:
        random.shuffle(self.train)

    def __repr__(self):
        return f"StorageTrain({len(self.train)} камер хранения)"
