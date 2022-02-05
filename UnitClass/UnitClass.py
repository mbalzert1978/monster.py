class UnitClass:
    def __init__(self) -> None:
        pass


class Paladin(UnitClass):
    def __init__(self) -> None:
        super().__init__()
        self.attack_min: int = 10
        self.attack_max: int = 10
        self.health: int = 100
        self.heal: int = 16


class Rogue(UnitClass):
    def __init__(self) -> None:
        super().__init__()
        self.attack_min: int = 5
        self.attack_max: int = 30
        self.health: int = 100


class Monster(UnitClass):
    def __init__(self) -> None:
        super().__init__()
        self.attack_min: int = 10
        self.attack_max: int = 20
        self.health: int = 100
