from random import randint
# final game v1
# def calc_monster_attack():
#     return randint(monster["attack_min"], monster["attack_max"])

def game_end(winner_name):
    print(f"{winner_name} won the game.")

def InputFunction(max_ele):
    """
    Funktion gibt einen wert zurück der max_ele entspricht nach input
    input wird auf max_ele geprüft und auf validität.
    max_ele = 0 : hier wird ein str zurückgegeben und (bsp Name_Spieler)
    max_ele = 1 : hier wird geprüft ob der spieler 1 eingegeben hat
    max_ele = 2 : hier wird geprüft ob der spieler 1 oder 2 eingegeben hat
    max_ele = 3 : hier wird geprüft ob der spieler 1 oder 2 oder 3 eingegeben hat
    max_ele = 4 : hier wird geprüft ob der spieler 1-4 eingegeben hat
    usw.
    
    """
    return "1"


game_running = True
game_result = []


while game_running == True:
    new_round = True
    player_won = False
    monster_won = False
    counter = 0
    player = {"name": "Marco", "attack": 10, "heal": 16, "health": 100}
    monster = {"name": "Mastodon", "attack_min": 10, "attack_max": 20, "health": 100}
    
    print("---" *7)
    print("Tell me the Name of your Hero: ")
    player["name"] = InputFunction(0)

    while new_round:
        counter = counter + 1
        print("---" *7)
        print("Please select an action")
        print("1) attack")
        print("2) heal")
        print("3) Exit game")
        print("4) show results")
        player_choice = InputFunction(4)

        if player_choice == "1":
            print(f"{player['name']} attacks monster for {player['attack']} damage")
            print("---" *7)
            monster["health"] = monster["health"] - player["attack"]
            
            if monster["health"] <= 0:
                player_won = True
            else:
                cma = randint(monster["attack_min"], monster["attack_max"])
                #cma = randint(monster.get("attack_min"), monster.get("attack_max")) ist auch möglich (läuft auch bei Fehlern durch)
                print(f'{monster["name"]} attacks {player["name"]} for {cma} damage')
                print("---" *7)
                player["health"] = player["health"] - cma
            
            if player["health"] <= 0:
                monster_won = True       

        elif player_choice == "2":
            cma = randint(monster["attack_min"], monster["attack_max"])
            print(f'{player["name"]} heals himself for {player["heal"]}')
            print("---" *7)
            player["health"] = player["health"] + player["heal"]
            print(f'{monster["name"]} attacks {player["name"]} for {cma} damage')
            print("---" *7)
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
            print("---" *7)
            print(f'{player["name"]} has {player["health"]} health left')
            print("---" *7)
            print("\n")
            print("---" *7)
            print(f'{monster["name"]} has {monster["health"]} health left')
            print("---" *7)
                
        elif player_won:
            game_end(player["name"])
            round_result = {"name": player["name"], "health": player["health"], "rounds": counter}
            game_result.append(round_result)
            new_round = False
                
        elif monster_won:
            game_end(monster["name"])
            round_result = {"name": player["name"], "health": player["health"], "rounds": counter}
            game_result.append(round_result)
            new_round = False

