import os, time
from random import randint

# final game v1
# def calc_monster_attack():
#     return randint(monster["attack_min"], monster["attack_max"])

def game_end(winner_name):
    print(f"{winner_name} won the game.")

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
    x = input()
    if MaxInt == 0:
        return "Player"
    try:
        x = int(x)
        if type(x) == int and x <= MaxInt and x >= 1:
            return str(x)
        else:
            print("Fehler:", end=" ")
            if x < 1 or x > MaxInt:
                print(f"Eingabe nicht im Bereich zwischen einschließlich 1 und {MaxInt}")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
            elif type(x) == float:
                print("Eingabe nur in GANZZAHLEN du IDIOT")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
            else:
                print("Der Scheiß war jetzt so heftig das ich nichtmal eine Fehlermeldung für dich habe")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
    except:
        print("Fehler:", end=" ")
        try:
            x = float(x)
            if type(x) == float:
                print("Eingabe nur in GANZZAHLEN du IDIOT")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
            else:
                print("Der Scheiß war jetzt so heftig das ich nichtmal eine Fehlermeldung für dich habe")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
        except:
            if x == "":
                print("Keine Eingabe ist auch ne Eingabe? was denkst du dir?")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
            elif type(x) == str:
                print("Eingabe keine Zahl sondern Text (String)")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
            elif type(x) == float:
                print("Eingabe nur in GANZZAHLEN du IDIOT")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)
            else:
                print("Der Scheiß war jetzt so heftig das ich nichtmal eine Fehlermeldung für dich habe")
                print("Bitte Eingabe korrekt wiederholen")
                return InputFunction(MaxInt)


game_running = True
game_result = []
os.system("cls")
print("---" *10)
print("Tell me the Name of your Hero: ")
player_name = InputFunction(0)

print("What Heroclass should your Hero be? (1) Rogue, or (2) Paladin: ")
player_class = InputFunction(2)

while game_running == True:
    new_round = True
    player_won = False
    monster_won = False
    counter = 0
    # 2 klassem eingefügt ohne den code zu brechen
    rogue = {"attack_min": 10, "attack_max": 40}
    paladin = {"attack": 20, "heal": 16}
    player = {"health": 100}
    
    monster = {"name": "Mastodon", "attack_min": 10, "attack_max": 20, "health": 100}


    while new_round:
        os.system("cls")
        counter = counter + 1
        if player_won == False and monster_won == False:
            os.system("cls")
            print("---" * 10)
            print(f'{player_name} has {player["health"]} health left')
            print("\n")
            print(f'{monster["name"]} has {monster["health"]} health left')
            print("---" * 10)
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
        print("\n")
        print("Please select an action")
        print("1) attack")
        print("2) heal")
        print("3) Exit game")
        print("4) show results")
        player_choice = InputFunction(4)

        if player_choice == "1":
            if player_class == "1":
                rogue_attack = randint(rogue["attack_min"], rogue["attack_max"])
                print(f"{player_name} attacks monster for {rogue_attack} damage")
                print("---" *10)
                monster["health"] = monster["health"] - rogue_attack
                time.sleep(1)
            elif player_class == "2":
                print(f"{player_name} attacks monster for {paladin['attack']} damage")
                print("---" *10)
                monster["health"] = monster["health"] - paladin["attack"]
                time.sleep(1)

            if monster["health"] <= 0:
                player_won = True
            else:
                cma = randint(monster["attack_min"], monster["attack_max"])
                print(f'{monster["name"]} attacks {player_name} for {cma} damage')
                print("---" *10)
                player["health"] = player["health"] - cma
                input("Enter for next round.")

            if player["health"] <= 0:
                monster_won = True

        elif player_choice == "2":
            if player_class == "2":
                cma = randint(monster["attack_min"], monster["attack_max"])
                print(f'{player_name} heals himself for {paladin["heal"]}')
                print("---" *10)
                player["health"] = player["health"] + paladin["heal"]
                print(f'{monster["name"]} attacks {player_name} for {cma} damage')
                print("---" *10)
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
            for element in game_result:
                os.system("cls")
                print(element)
                input("Enter for new Game/next Round")

        else:
            print("Invalid input")


