import random
import json

import rich
import rich.prompt

from . import shop
from . import terminal

storyline = json.load(open("./src/storyline.json", "r", encoding="utf-8"))

database = {}

player = {"credits": 0, "food": 0, "parts": 0, "arms": 0}

def check_variable(test):

    global database

    if test[0] == "$":

        if test[1:] in database.keys():

            return database[test[1:]]
        
        else:

            return test[1:]
    
    else:

        return test

def run_sequence(sequence, tstt):

    global database, player

    idx = 0

    while True:

        if len(sequence) < idx + 1: break

        if " " in sequence[idx]:
            split_sequence = sequence[idx].split(" ")
        else:
            split_sequence = [sequence[idx]]
        
        print(sequence[idx])

        if sequence[idx][0] == "!":

            if split_sequence[0] == "!jump_switch":

                return sequence[idx+1][database[split_sequence[1]]]
            
            elif split_sequence[0] == "!store":

                database[split_sequence[1]] = check_variable(split_sequence[2])
            
            elif split_sequence[0] == "!credits":

                player["credits"] = player["credits"] + (1 if split_sequence[1] == "+" else -1) * int(split_sequence[2])
            
            if split_sequence[0] == "!jump":
                
                return split_sequence[1]

            if split_sequence[0] == "!slow":

                tstt.slowprint(" ".join(split_sequence[2:]), letters_per_second=int(split_sequence[1]))
            
            if split_sequence[0] == "!end":

                return "end"

            if split_sequence[0] == "!modify": # checks for what player value it's modifying then the amount to modify by then the operation for modification
                player_value = player[split_sequence[1]]
                mod_value = int(split_sequence[3])

                if split_sequence[2] == "+":
                    player[split_sequence[1]] += mod_value
                elif split_sequence[2] == "-":
                    player[split_sequence[1]] -= mod_value
                elif split_sequence[2] == "/":
                    player[split_sequence[1]] *= mod_value
                elif split_sequence[2] == "/":
                    player[split_sequence[1]] /= mod_value

            if split_sequence[0] == "!hop_random":

                print(split_sequence)

                return random.choice(split_sequence[1:])

            if split_sequence[0] == "!if":

                if split_sequence[1] == ">=":

                    if player[split_sequence[2]] >= int(split_sequence[3]):

                        return run_sequence(sequence[idx+2])
                    
                    else:

                        return run_sequence(sequence[idx+1])
                
                if split_sequence[1] == "<=":

                    if player[split_sequence[2]] <= int(split_sequence[3]):

                        return run_sequence(sequence[idx+2])
                    
                    else:

                        return run_sequence(sequence[idx+1])


            if split_sequence[0] == "!shop":

                shop_obj_json = sequence[idx+1]

                shop_obj = shop.shop(
                    tstt,

                    title=shop_obj_json["title"], 
                    store_keeper_name=shop_obj_json["store_keeper_name"], 
                    store_keeper_msg=shop_obj_json["store_keeper_msg"],

                    player=player
                    )

                for item_obj_json in sequence[idx+1]["items"]:

                    shop_obj.add_items([
                        shop.Item(name=item_obj_json["name"], emoji=item_obj_json["emoji"], price=item_obj_json["price"], id=item_obj_json["id"])
                    ])
                
                idx += 1

                shop_obj.run()
        
        elif sequence[idx][0] == "#":
            pass

        else:

            if sequence[idx][0] == "?":



                rich.print(sequence[idx][1:])
                
                if type(sequence[idx+1]) == list:
                    database["choice"] = rich.prompt.Prompt.ask("?> ", choices=sequence[idx+1])
                
                elif type(sequence[idx+1]) == dict:
                    database["choice"] = rich.prompt.Prompt.ask("?> ", choices=sequence[idx+1].keys())
                    return sequence[idx+1][database["choice"]]

                idx += 1

            else:

                rich.print(sequence[idx]) 

        idx += 1
    
def execute_parse(console: rich.Console):

    global storyline

    tstt = terminal.terminal(console)

    state = run_sequence(storyline["intro"], tstt)

    while True:

        new_state = run_sequence(storyline[state], tstt)

        if new_state == "end":

            break

        else:

            state = new_state

execute_parse(rich.get_console())
