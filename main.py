import os
import time
import random
import platform

CLEAR = True


class Entity:
    name: str
    health: int
    attack_min: int
    attack_max: int

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


def main(monster: Monster) -> None:
    game_running = True
    game_result = []
    clear_screen()
    player_name = input("Tell me the Name of your Hero: ")
    clear_screen()
    print("What Heroclass should your Hero be?")
    player_choice = input("Rogue, or Paladin: ")
    player = create_player(player_name, player_choice)

    while game_running:
        new_round = True
        player_won = False
        monster_won = False
        rounds_played = 0
        while new_round:
            rounds_played += 1
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
                    "rounds": rounds_played,
                }
                game_result.append(round_result)
                new_round = False
            else:
                game_end(monster.name)
                round_result = {
                    "name": player.name,
                    "health": player.health,
                    "rounds": rounds_played,
                }
                game_result.append(round_result)
                new_round = False
            input("Enter for next round.")
            clear_screen()
            draw_menu()
            match input():
                case "1":
                    clear_screen()
                    attack_roll = calculate_attack(player)
                    draw_player_attack(player, attack_roll)
                    calculate_damage(monster, attack_roll)
                    if monster.health <= 0:
                        player_won = True
                    else:
                        attack_roll = calculate_attack(monster)
                        draw_monster_attack(monster, player, attack_roll)
                        calculate_damage(player, attack_roll)
                    if player.health <= 0:
                        monster_won = True
                        input("Enter for next round.")
                case "2":
                    if isinstance(player, PaladinClass):
                        attack_roll = random.randint(
                            monster.attack_min, monster.attack_max
                        )
                        print(
                            f"{player.name} heals himself for {player.heal}\n\n"
                            f"{monster.name} attacks {player.name} for "
                            f"{attack_roll} damage"
                        )
                        player.health += player.heal
                        player.health -= attack_roll
                        input("Enter for next round.")
                    else:
                        print("Rogues cant heal:)")
                        time.sleep(1)
                case "3":
                    new_round = False
                    game_running = False
                    break
                case "4":
                    highscore = ""
                    for element in game_result:
                        for key, value in element.items():
                            highscore += f"{key} : {value}\n"
                    print(highscore)
                    input("Enter for new Game\nnext Round")
                    clear_screen()
                case _:
                    print("Invalid input")


def draw_monster_attack(
    monster: Entity, player: Entity, attack_roll: int
) -> None:
    """Draws the monster's attack"""
    print(f"{monster.name} attacks {player.name} for {attack_roll} damage")


def draw_player_attack(player: Entity, attack_roll: int) -> None:
    """Draws the attack roll on the screen."""
    print(f"{player.name} attacks monster for {attack_roll} damage.")


def calculate_damage(entitiy: Entity, attack_roll: int) -> None:
    """Substracts the damage dealt."""
    entitiy.health -= attack_roll


def calculate_attack(entity: Entity) -> int:
    """
    Evaluate the entity attackvalue.

    Args:
        entity: The entity object.

    Returns:
        The damage dealt.
    """
    return random.randint(entity.attack_min, entity.attack_max)


def create_player(player_name: str, player_choice: str) -> Entity:
    """
    Creates a player object.

    Args:
        player_name: The name of the player.
        player_choice: Class choice of the player.

    Returns:
        A Player entity.
    """
    while True:
        match player_choice.lower():
            case "rogue":
                return player_class_factory[player_choice](name=player_name)
            case "paladin":
                return player_class_factory[player_choice](name=player_name)
            case _:
                print(f"I don't know {player_choice}")


def draw_menu() -> None:
    """Draws the menu."""
    print(
        "Please select an action\n"
        "1) attack\n"
        "2) heal\n"
        "3) Exit game\n"
        "4) show results\n"
    )


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
    monster = Monster()
    main(monster)
