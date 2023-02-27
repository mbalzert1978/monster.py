import os
import time
import random
import platform

CLEAR = True


class Entity:
    name: str
    health: int

    def __init__(self, name="Player", health=100) -> None:
        self.name = name
        self.health = health


class Monster(Entity):
    monster_names = ["Goblin", "Skeleton", "Zombie"]

    def __init__(self, health=80) -> None:
        super().__init__(random.choice(self.monster_names), health)
        self.attack_min = 10
        self.attack_max = 20
        self.health = health


class RogueClass(Entity):
    def __init__(self, name="Player", health=80) -> None:
        super().__init__(name)
        self.attack_min = 5
        self.attack_max = 40
        self.health = health


class PaladinClass(Entity):
    def __init__(self, name="Player", health=120) -> None:
        super().__init__(name)
        self.attack_min = 5
        self.attack_max = 15
        self.health = health
        self.heal = 20


player_class_factory = {"rogue": RogueClass, "paladin": PaladinClass}


def game_end(winner_name) -> None:
    print(f"{winner_name} won the game.")


def main() -> None:
    game_running = True
    game_result = []
    clear_screen()
    player_name = input("Tell me the Name of your Hero: ")
    clear_screen()
    print("What Heroclass should your Hero be?")
    player_choice = input("Rogue, or Paladin: ")
    player = create_player(player_name, player_choice)
    monster = Monster()

    while game_running:
        new_round = True
        player_won = False
        monster_won = False
        counter = 0
        while new_round:
            counter += 1
            if not player_won and not monster_won:
                print(
                    f"{player.name} has {player.health} "
                    f"health left\n\n{monster.name} has "
                    f"{monster.health} health left"
                )
            elif player_won:
                game_end(player.name)
                round_result = {
                    "name": player.name,
                    "health": player.health,
                    "rounds": counter,
                }
                game_result.append(round_result)
                new_round = False
            else:
                game_end(monster.name)
                round_result = {
                    "name": player.name,
                    "health": player.health,
                    "rounds": counter,
                }
                game_result.append(round_result)
                new_round = False
            input("Enter for next round.")
            clear_screen()
            player_choice = input(
                "Please select an action\n"
                "1) attack\n"
                "2) heal\n"
                "3) Exit game\n"
                "4) show results\n"
            )
            clear_screen()
            if player_choice == "1":
                clear_screen()
                player_attack_random = random.randint(
                    player.attack_min, player.attack_max
                )
                print(
                    f"{player.name} attacks monster for "
                    f"{player_attack_random} damage"
                )
                monster.health -= player_attack_random
                if monster.health <= 0:
                    player_won = True
                else:
                    monster_attack_random = random.randint(
                        monster.attack_min, monster.attack_max
                    )
                    print(
                        f"{monster.name} attacks {player.name} for "
                        f"{monster_attack_random} damage"
                    )
                    player.health -= monster_attack_random
                if player.health <= 0:
                    monster_won = True
                    input("Enter for next round.")
            elif player_choice == "2":
                if isinstance(player, PaladinClass):
                    monster_attack_random = random.randint(
                        monster.attack_min, monster.attack_max
                    )
                    print(
                        f"{player.name} heals himself for {player.heal}\n\n"
                        f"{monster.name} attacks {player.name} for "
                        f"{monster_attack_random} damage"
                    )
                    player.health += player.heal
                    player.health -= monster_attack_random
                    input("Enter for next round.")
                else:
                    print("Rogues cant heal:)")
                    time.sleep(1)
            elif player_choice == "3":
                new_round = False
                game_running = False
                break

            elif player_choice == "4":
                highscore = ""
                for element in game_result:
                    for key, value in element.items():
                        highscore += f"{key} : {value}\n"
                print(highscore)
                input("Enter for new Game\nnext Round")
                clear_screen()
            else:
                print("Invalid input")


def create_player(player_name: str, player_choice: str) -> Entity:
    while True:
        match player_choice.lower():
            case "rogue":
                return player_class_factory[player_choice](name=player_name)
            case "paladin":
                return player_class_factory[player_choice](name=player_name)
            case _:
                print(f"I don't know {player_choice}")


def clear_screen(clear: bool = CLEAR) -> None:
    """Clears the screen."""
    if not clear:
        return
    match platform.system().lower():
        case "windows":
            os.system("cls")
        case "linux":
            os.system("clear")
        case "darwin":
            os.system("clear")
        case _:
            print("OS not supported. Not clearing screen.")
            clear = False


if __name__ == "__main__":
    main()
