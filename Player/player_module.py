"""
player modul
"""
import random
from UnitClass.UnitClass import Paladin, Rogue, Monster


class Player:
    """
    player class
    attributes:
    attack_min
    attack_max
    health
    heal
    """

    def __init__(self) -> None:
        self.attack_min = None
        self.attack_max = None
        self.health = None
        self.heal = None

    def get_move(self, player, target) -> None:
        """
        interface for get_move
        """

    def set_attributes(self, class_) -> None:
        """
        sets attributes in class
        """
        self.attack_min = class_.attack_min
        self.attack_max = class_.attack_max
        self.health = class_.health
        if hasattr(class_, "heal"):
            self.heal = class_.heal


class RandomComputerPlayer(Player):
    """
    computerplayer class who picks random
    """

    def __init__(self, name: str = None) -> None:
        super().__init__()
        self.name = (
            random.choice(["Hal9000", "T-800", "ED-209", "M.A.R.K.13"])
            if not name
            else name
        )
        # if not name:
        #     self.name = random.choice(
        #         ["Hal9000", "T-800", "ED-209", "M.A.R.K.13"]
        #     )
        # else:
        #     self.name = name
        self.choose_class()

    def choose_class(self) -> None:
        """
        CPU chooses random class
        """
        choosen_class = random.choice([Rogue, Paladin, Monster])()
        self.set_attributes(choosen_class)

    def get_move(self, player, target=None) -> int:
        return random.choice([1, 2]) if player.heal is not None else 1


class BetterComputerPlayer(Player):
    """
    hopefully a better CPU player
    """

    def __init__(self, name: str = None) -> None:
        super().__init__()
        self.name = (
            random.choice(["Hal9000", "T-800", "ED-209", "M.A.R.K.13"])
            if not name
            else name
        )
        self.choose_class()

    def choose_class(self) -> None:
        """
        always chooses paladin class for selfheal
        """
        choosen_class = Paladin()
        self.set_attributes(choosen_class)

    def get_move(self, player, target=None) -> int:
        return 2 if player.health <= 35 and target.health >= 10 else 1


class HumanPlayer(Player):
    """
    Human player class
    and print statements to explain the game
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = input("Tell me the Name of your Hero: ")
        self.choose_class()

    def choose_class(self) -> None:
        """
        lets the player choose a class
        """
        user_input = self.get_input(
            [1, 2], "What Class you want to play?", "Paladin(1) or Rogue(2): "
        )
        class_ = [Paladin, Rogue]
        self.set_attributes(class_[user_input - 1]())

    @staticmethod
    def get_input(valid: list, decorator: str, question: str) -> int:
        """
        checks user input and returns user input as int
        """
        while True:
            print(decorator)
            try:
                val = int(input(question))
                if val in valid:
                    return val
                raise ValueError
            except ValueError:
                print("No valid choice, try again.")

    def get_move(self, player, target=None) -> int:
        return self.get_input(
            [1, 2],
            "What do you want to do?",
            "attack(1) or heal(2): "
            if player.heal is not None
            else "attack(1): ",
        )
