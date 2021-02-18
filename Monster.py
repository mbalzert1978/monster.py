import os, time
from random import randint

# final game v1
# def calc_monster_attack():
#     return randint(monster["attack_min"], monster["attack_max"])

def game_end(winner_name):
    new_print(f"{winner_name} won the game.", "m")

def InputFunction(MaxInt):
    """
    funktion InputFunction(str_check)
    die funktion bekommt einen str_check mit value:
    bei str_check 0 soll die funktion die player_input zurückgeben bei player_input "" wird "player" als default zurückgegeben.
    bei str_check 1 wird geprüft ob player_input 1 ist und nichts anderes ist erlaubt.
    bei str_check 2 wird geprüft ob player_input 1 oder 2 ist und nichts anderes ist erlaubt.
    bei str_check 3 wird geprüft ob player_input 1 oder 2 oder 3 ist und nichts anderes ist erlaubt.
    bei str_check 4 wird geprüft ob player_input 1 oder 2 oder 3 oder 4 ist und nichts anderes ist erlaubt.
    """
    player_input = input()
    if MaxInt == 0:
        if player_input == "":
            return "Player"
        else:
            return player_input
    try:
        player_input = int(player_input)
        if type(player_input) == int and player_input <= MaxInt and player_input >= 1:
            return str(player_input)
        else:
            print("Fehler:", end=" ")
            if player_input < 1 or player_input > MaxInt:
                print(f"Eingabe nicht im Bereich zwischen einschließlich 1 und {MaxInt}")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
            else:
                print("Der Scheiß war jetzt so heftig, dass ich nichtmal eine Fehlermeldung für dich habe")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
    except ValueError or TypeError:               #<--- bitteschön
        print("Incorect input:", end=" ")
        return InputFunction(MaxInt)


def new_print(text, zentriert):        # text mit /n für mehrere zeilen
    text = str(text)                    #zentriert mit M= jede zeile gemittelt
    text = text.split("/n")             #R= jede zeile rechts bündig
    maxLen = 0                          #L= jede zeile links bündig
    for i in range(len(text)):
        x = len(text[i])
        if x > maxLen:
            maxLen = x
    check = ["M", "R", "L", "m", "r", "l"]
    if zentriert not in check:
        return "Fehler im new_print"
    print("+", "-" * 110, "+", sep="")
    for i in range(12-len(text)//2):
        print("|", " "*110, "|", sep="")
    if zentriert == "M" or zentriert == "m":
        for row in range(len(text)):
            if len(text[row]) % 2 == 0:
               print("|", " "*(55 - (len(text[row])//2)), text[row], " "*(55 - (len(text[row])//2)), "|", sep="")
            else:
                print("|", " "*(55 - (len(text[row])//2)), text[row], " "*(54 - (len(text[row])//2)), "|", sep="")
    elif zentriert == "L" or zentriert == "l":
        for row in range(len(text)):
            if maxLen % 2 == 0:
                print("|", " "*(55-(maxLen//2)), text[row], " "*(55 + maxLen -(maxLen//2) - len(text[row])), "|", sep="")
            else:
                print("|", " "*(55-(maxLen//2)), text[row], " "*(54 + maxLen -(maxLen//2) - len(text[row])), "|", sep="")
    else:
        for row in range(len(text)):
            if maxLen % 2 == 0:
               print("|", " "*(55 + maxLen -(maxLen//2) - len(text[row])), text[row], " "*(55-(maxLen//2)), "|", sep="")
            else:
               print("|", " "*(54 + maxLen -(maxLen//2) - len(text[row])), text[row], " "*(55-(maxLen//2)), "|", sep="")
    if len(text) % 2 == 0:
        for i in range(12-len(text)//2):
            print("|", " "*110, "|", sep="")
    else:
        for i in range(12-(len(text)//2)-1):
            print("|", " "*110, "|", sep="")
    print("+", "-" * 110, "+", sep="")


game_running = True
game_result = []
os.system("cls")
new_print("Tell me the Name of your Hero:", "m")
player_name = InputFunction(0)
os.system("cls")
new_print("What Heroclass should your Hero be? (1) Rogue, or (2) Paladin:", "m")
player_class = InputFunction(2)


while game_running == True:
    new_round = True
    player_won = False
    monster_won = False
    counter = 0
    rogue = {"attack_min": 10, "attack_max": 40}
    paladin = {"attack": 10, "heal": 16}
    player = {"health": 100}
    monster = {"name": "Mastodon", "attack_min": 10, "attack_max": 20, "health": 100}

    while new_round:
        os.system("cls")
        counter = counter + 1
        if player_won == False and monster_won == False:
            new_print(f'{player_name} has {player["health"]} health left/n /n{monster["name"]} has {monster["health"]} health left', "m")

        elif player_won:
            game_end(player_name)
            round_result = {"name": player_name, "health": player["health"], "rounds": counter}
            game_result.append(round_result)
            new_round = False

        elif monster_won:
            game_end(monster["name"])
            round_result = {"name": player_name, "health": player["health"], "rounds": counter}
            game_result.append(round_result)
            new_round = False
        input("Enter for next round.")
        os.system("cls")
        new_print("Please select an action/n1) attack/n2) heal/n3) Exit game/n4) show results", "l")
        player_choice = InputFunction(4)
        os.system("cls")
        if player_choice == "1":
            if player_class == "1":
                rogue_attack = randint(rogue["attack_min"], rogue["attack_max"])
                cache_pattack = f"{player_name} attacks monster for {rogue_attack} damage"
                monster["health"] = monster["health"] - rogue_attack
            elif player_class == "2":
                cache_pattack = f"{player_name} attacks monster for {paladin['attack']} damage"
                monster["health"] = monster["health"] - paladin["attack"]
            if monster["health"] <= 0:
                player_won = True
            else:
                os.system("cls")
                cma = randint(monster["attack_min"], monster["attack_max"])
                new_print(f'{monster["name"]} attacks {player_name} for {cma} damage/n /n{cache_pattack}', "m")
                player["health"] = player["health"] - cma
                input("Enter for next round.")
            if player["health"] <= 0:
                monster_won = True

        elif player_choice == "2":
                if player_class == "2":
                    cma = randint(monster["attack_min"], monster["attack_max"])
                    new_print(f'{player_name} heals himself for {paladin["heal"]}/n /n{monster["name"]} attacks {player_name} for {cma} damage', "m")
                    player["health"] = player["health"] + paladin["heal"]
                    player["health"] = player["health"] - cma
                    input("Enter for next round.")
                else:
                    new_print("Rogues cant heal :)", "m")
                    time.sleep(1)
        elif player_choice == "3":
            new_round = False
            game_running = False
            break

        elif player_choice == "4":
            highscore = ""
            for element in game_result:
                for a, b in element.items(): 
                    highscore += f"{a} : {b}/n"
            new_print(highscore, "l")
            input("Enter for new Game/next Round")
        else:
            new_print("Invalid input", "m")
