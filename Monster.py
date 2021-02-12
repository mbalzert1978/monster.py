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
        return x
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
print("---" * 7)
print("Tell me the Name of your Hero: ")
player_name = InputFunction(0)

while game_running == True:
    new_round = True
    player_won = False
    monster_won = False
    counter = 0
    # 2 klassem eingefügt ohne den code zu brechen
    rogue = {"attack_min": 10, "attack_max": 30, "health": 100}
    warrior = {"attack": 20, "heal": 16, "health": 100}
    player = {"attack": 10, "heal": 16, "health": 100}
    
    monster = {"name": "Mastodon", "attack_min": 10, "attack_max": 20, "health": 100}


    while new_round:
        counter = counter + 1
        print("---" * 7)
        print("Please select an action")
        print("1) attack")
        print("2) heal")
        print("3) Exit game")
        print("4) show results")
        player_choice = InputFunction(4)

        if player_choice == "1":
            print(f"{player_name} attacks monster for {player['attack']} damage")
            print("---" * 7)
            monster["health"] = monster["health"] - player["attack"]

            if monster["health"] <= 0:
                player_won = True
            else:
                cma = randint(monster["attack_min"], monster["attack_max"])
                # cma = randint(monster.get("attack_min"), monster.get("attack_max")) ist auch möglich (läuft auch bei Fehlern durch)
                print(f'{monster["name"]} attacks {player_name} for {cma} damage')
                print("---" * 7)
                player["health"] = player["health"] - cma

            if player["health"] <= 0:
                monster_won = True

        elif player_choice == "2":
            cma = randint(monster["attack_min"], monster["attack_max"])
            print(f'{player_name} heals himself for {player["heal"]}')
            print("---" * 7)
            player["health"] = player["health"] + player["heal"]
            print(f'{monster["name"]} attacks {player_name} for {cma} damage')
            print("---" * 7)
            player["health"] = player["health"] - cma

            if player["health"] <= 0:
                monster_won = True

        elif player_choice == "3":
            new_round = False
            game_running = False

        elif player_choice == "4":
            for element in game_result:
                print(element)

        else:
            print("Invalid input")

        if player_won == False and monster_won == False:
            print("---" * 7)
            print(f'{player_name} has {player["health"]} health left')
            print("---" * 7)
            print("\n")
            print("---" * 7)
            print(f'{monster["name"]} has {monster["health"]} health left')
            print("---" * 7)
        elif player_won:
            game_end(player["name"])
            round_result = {"name": player_name, "health": player["health"], "rounds": counter}
            game_result.append(round_result)
            new_round = False

        elif monster_won:
            game_end(monster["name"])
            round_result = {"name": player_name, "health": player["health"], "rounds": counter}
            game_result.append(round_result)
            new_round = False


