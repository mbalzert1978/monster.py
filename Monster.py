from random import randint
<<<<<<< Updated upstream
=======

# Kommentar von Karsten
>>>>>>> Stashed changes
# final game v1
# def calc_monster_attack():
#     return randint(monster["attack_min"], monster["attack_max"])

def game_end(winner_name):
    print(f"{winner_name} won the game.")

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
    player["name"] = input()

    while new_round == True:
        counter = counter + 1
        print("---" *7)
        print("Please select an action")
        print("1) attack")
        print("2) heal")
        print("3) Exit game")
        print("4) show results")
        player_choice = input()

        if player_choice == "1":
            print(player["name"] + " attacks monster for " + str(player["attack"]) +" damage")
            print("---" *7)
            monster["health"] = monster["health"] - player["attack"]
            
            if monster["health"] <= 0:
                player_won = True
            else:
                cma = randint(monster["attack_min"], monster["attack_max"])
                #cma = randint(monster.get("attack_min"), monster.get("attack_max")) ist auch möglich (läuft auch bei Fehlern durch)
                print(monster["name"] + " attacks " + player["name"] + " for " + str(cma) +" damage")
                print("---" *7)
                player["health"] = player["health"] - cma
            
            if player["health"] <= 0:
                monster_won = True       

        elif player_choice == "2":
            cma = randint(monster["attack_min"], monster["attack_max"])
            print(player["name"] + " heals himself for " + str(player["heal"]))
            print("---" *7)
            player["health"] = player["health"] + player["heal"]
            
            print(monster["name"] + " attacks " + player["name"] + " for " + str(cma) +" damage")
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
            print(player["name"] + " has " + str(player["health"]) + " health left")
            print("---" *7)
            print("\n")
            print("---" *7)
            print(monster["name"] + " has " + str(monster["health"]) + " health left")
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

# Hat das geklappt?
# Gebraddel und Geballer