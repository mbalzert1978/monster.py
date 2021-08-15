import os
import time
import random


def game_end(winner_name):
    print(f"{winner_name} won the game.")


def main():
    game_running = True
    game_result = []
    os.system("cls")
    player_name = input("Tell me the Name of your Hero: ") or "Player"
    os.system("cls")
    player_class = input("What Heroclass should your Hero be?\
\n (1) Rogue, or \n (2) Paladin: ")

    while game_running:
        new_round = True
        player_won = False
        monster_won = False
        counter = 0
        rogue = {"attack_min": 10, "attack_max": 40}
        paladin = {"attack_min": 5, "attack_max": 20, "heal": 16}
        player = {"health": 100}
        monster = {"name": "Mastodon",
                   "attack_min": 10,
                   "attack_max": 20,
                   "health": 100}

        while new_round:
            counter = counter + 1
            if not player_won and not monster_won:
                os.system("cls")
                print(f'{player_name} has {player["health"]} health left\n\
{monster["name"]} has {monster["health"]} health left')

            elif player_won:
                game_end(player_name)
                round_result = {"name": player_name,
                                "health": player["health"],
                                "rounds": counter}
                game_result.append(round_result)
                new_round = False

            elif monster_won:
                game_end(monster["name"])
                round_result = {"name": player_name,
                                "health": player["health"],
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
                if player_class == "1":
                    rogue_attack = random.randint(rogue["attack_min"],
                                                  rogue["attack_max"])
                    print(f"{player_name} attacks \
monster for {rogue_attack} damage")
                    monster["health"] = monster["health"] - rogue_attack
                elif player_class == "2":
                    paladin_attack = random.randint(paladin["attack_min"],
                                                    paladin["attack_max"])
                    print(f"{player_name} attacks \
monster for {paladin_attack} damage")
                    monster["health"] = monster["health"] - paladin_attack

                if monster["health"] <= 0:
                    player_won = True
                else:
                    cma = random.randint(monster["attack_min"],
                                         monster["attack_max"])
                    print(f'{monster["name"]} attacks \
{player_name} for {cma} damage')
                    player["health"] = player["health"] - cma
                    input("Enter for next round.")
                if player["health"] <= 0:
                    monster_won = True

            elif player_choice == "2":
                if player_class == "2":
                    cma = random.randint(monster["attack_min"],
                                         monster["attack_max"])
                    print(f'{player_name} heals himself for {paladin["heal"]} \
{monster["name"]} attacks \
{player_name} for {cma} damage')
                    player["health"] = player["health"] + paladin["heal"]
                    player["health"] = player["health"] - cma
                    input("Enter for next round.")
                else:
                    print("Rogues cant heal :)")
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
                input("Enter for new Game or \
next Round")
            else:
                print("Invalid input")


if __name__ == "__main__":
    main()
