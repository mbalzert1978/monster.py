import os
import time
from random import randint


class Entity:

    name: str

    def __init__(self, name="Player") -> None:
        self.name = name


class Monster(Entity):

    name: str
    health: int

    def __init__(self, name, health=100) -> None:
        super().__init__(name)
        self.attack_min = 10
        self.attack_max = 20
        self.health = health


class RogueClass(Entity):

    name: str
    health: int

    def __init__(self, name, health=80) -> None:
        super().__init__(name)
        self.attack_min = 5
        self.attack_max = 40
        self.health = health


class PaladinClass(Entity):

    name: str
    health: int
    heal: int

    def __init__(self, name, health=120) -> None:
        super().__init__(name)
        self.attack_min = 5
        self.attack_max = 15
        self.health = health
        self.heal = 20


def game_end(winner_name):
    print(f"{winner_name} won the game.")


def main():
    game_running = True
    game_result = []
    os.system("cls")
    player_name = input("Tell me the Name of your Hero: ")
    os.system("cls")
    player_class = input(
        "What Heroclass should your Hero be? (1) Rogue, or (2) Paladin: "
        )
    player = RogueClass(player_name) \
        if player_class == "1" else PaladinClass(player_name)
    monster = Monster("Mastodon")

    while game_running:
        new_round = True
        player_won = False
        monster_won = False
        counter = 0
        while new_round:
            counter += 1
            if not player_won and not monster_won:
                print(f'{player.name} has {player.health} health left\n\n\
{monster.name} has {monster.health} health left')
            elif player_won:
                game_end(player.name)
                round_result = {"name": player.name,
                                "health": player.health,
                                "rounds": counter}
                game_result.append(round_result)
                new_round = False
            elif monster_won:
                game_end(monster.name)
                round_result = {"name": player.name,
                                "health": player.health,
                                "rounds": counter}
                game_result.append(round_result)
                new_round = False
            input("Enter for next round.")
            os.system("cls")
            player_choice = input("Please select an action\n\
                                   1) attack\n\
                                   2) heal\n\
                                   3) Exit game\n\
                                   4) show results\n")
            os.system("cls")
            if player_choice == "1":
                player_attack_random = randint(player.attack_min,
                                               player.attack_max)
                print(f"{player.name} attacks\
                        monster for {player_attack_random} damage")
                monster.health -= player_attack_random
                if monster.health <= 0:
                    player_won = True
                else:
                    os.system("cls")
                    monster_attack_random = randint(monster.attack_min,
                                                    monster.attack_max)
                    print(f'{monster.name} attacks\
                            {player.name} for {monster_attack_random} damage')
                    player.health -= monster_attack_random
                if player.health <= 0:
                    monster_won = True
                    input("Enter for next round.")
            elif player_choice == "2":
                if type(player) == PaladinClass:
                    monster_attack_random = randint(monster.attack_min,
                                                    monster.attack_max)
                    print(f'{player.name} heals himself for {player.heal}\n\n\
                            {monster.name} attacks {player.name} for\
                            {monster_attack_random} damage')
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
                    for a, b in element.items():
                        highscore += f"{a} : {b}\n"
                print(highscore)
                input("Enter for new Game\nnext Round")
            else:
                print("Invalid input")


if __name__ == "__main__":
    main()
