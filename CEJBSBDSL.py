# Built-in Libraries
import argparse
import json
import random
import time
import sys

CEJBSBDSL_VERSION = "0.5.0"

def error(error_message, code, warning=False):

    print(f'CEJBSBDSL {CEJBSBDSL_VERSION} {"Error" if not warning else "Warning"} (Code {code}): {error_message}')
    sys.exit(1)

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help="path to script")
parser.add_argument("-e", "--entry-point", default="init", required=False, help="program entry point")
parser.add_argument("-s", "--seed", default="42", required=False, help="random seed")
parser.add_argument("-v", "--version", action="version", version=CEJBSBDSL_VERSION)

args = parser.parse_args()

try:
    random.seed(int(args.seed))
except:
    error("Invalid seed provided.", "4")


origin_sequence = json.load(open(args.file, "r", encoding="utf-8"))

database = {} # Specifically for choice

# Check if some name is in the database; if it is, return the value 
def check_variable(test):

    global database

    if test[0] == "$":

        if test[1:] in database.keys():

            return database[test[1:]]
        
        else:

            return test[1:]
    
    else:

        return test

def prompt(text, choices, case_sensitive=False):

    while True:

        i = input(text)
        if not case_sensitive: i = i.lower()

        if i in choices:

            return i

# Run a sequence from storyline.json, run any commands that occur, ignore comments, 
# and auto-print anything that does not start with a special character
def run_sequence(sequence, database):

    idx = 0

    # Loop continuously until broken
    while True:

        if len(sequence) < idx + 1: break # Make sure it does not go forever

        # Split input for parsing
        if " " in sequence[idx]:
            split_sequence = sequence[idx].split(" ")
        else:
            split_sequence = [sequence[idx]]

        # Commands

        try:

            if sequence[idx][0] == "!":

                if split_sequence[0] == "!jump_switch":

                    return sequence[idx+1][database[split_sequence[1]]]
                
                elif split_sequence[0] == "!store":

                    database[split_sequence[1]] = check_variable(split_sequence[2])
                
                elif split_sequence[0] == "!jump":
                    
                    return split_sequence[1]

                # Ends WHOLE game
                elif split_sequence[0] == "!end":

                    sys.exit(0)

                elif split_sequence[0] == "!modify": # checks for what player value it's modifying then the amount to modify by then the operation for modification
                    if not split_sequence[1] in database.keys(): database[split_sequence[1]] = 0

                    mod_value = int(split_sequence[3])

                    if split_sequence[2] == "+":
                        database[split_sequence[1]] += mod_value
                    elif split_sequence[2] == "-":
                        database[split_sequence[1]] -= mod_value
                    elif split_sequence[2] == "/":
                        database[split_sequence[1]] *= mod_value
                    elif split_sequence[2] == "/":
                        database[split_sequence[1]] /= mod_value

                elif split_sequence[0] == "!random_hop": # Hops randomly

                    return random.choice(split_sequence[1:])

                elif split_sequence[0] == "!if": # If statement proxy

                    if split_sequence[2] == ">=":

                        if database[split_sequence[1]] >= int(split_sequence[3]):

                            return run_sequence(sequence[idx+2])
                        
                        else:

                            return run_sequence(sequence[idx+1])
                    
                    if split_sequence[2] == "<=":

                        if database[split_sequence[1]] <= int(split_sequence[3]):

                            return run_sequence(sequence[idx+2])
                        
                        else:

                            return run_sequence(sequence[idx+1])

                                    
                    if split_sequence[2] == "==":

                        if database[split_sequence[1]] == int(split_sequence[3]):

                            return run_sequence(sequence[idx+2])
                        
                        else:

                            return run_sequence(sequence[idx+1])

                    if split_sequence[2] == "!=":

                        if database[split_sequence[1]] == int(split_sequence[3]):

                            return run_sequence(sequence[idx+2])
                        
                        else:

                            return run_sequence(sequence[idx+1])
                    
                    if split_sequence[2] == ">":

                        if database[split_sequence[1]] > int(split_sequence[3]):

                            return run_sequence(sequence[idx+2])
                        
                        else:

                            return run_sequence(sequence[idx+1])
                    
                    if split_sequence[2] == "<":

                        if database[split_sequence[1]] < int(split_sequence[3]):

                            return run_sequence(sequence[idx+2])
                        
                        else:

                            return run_sequence(sequence[idx+1])

                else:

                    error(f"Command not found \"{split_sequence[0]}\".", 3)

            # Comment; pass
            elif sequence[idx][0] == "#":
                pass

            else:
                
                # Prompts user, jumps when it is a dict of options, otherwise sets choice to value
                if sequence[idx][0] == "?":

                    print(sequence[idx][1:])
                    
                    if type(sequence[idx+1]) == list:
                        database["choice"] = prompt("?> ", choices=sequence[idx+1], case_sensitive=False)
                    
                    elif type(sequence[idx+1]) == dict:
                        database["choice"] = prompt("?> ", choices=list(sequence[idx+1].keys()), case_sensitive=False)
                        return sequence[idx+1][database["choice"]]

                    idx += 1

                else:

                    time.sleep(1)

                    print(sequence[idx]) 

            idx += 1
        
        except IndexError:

            error(f"Critical command failure command \"{split_sequence[0]}\" given incorrect arguments")
        
        except Exception as e:

            error("Unknown error \"{e}\".", "?")
    
def check_state(state, origin_sequence):

    if state == None:

        error("No end call; assuming this is intentional and exiting.", "1", warning=True)

    elif state not in origin_sequence.keys():

            error(f"State \"{state}\" not found.", 1)
    
            exit(1)


# Runs main terminal, loop, iteratively running each sequence until the game is compelte
def execute_parse(origin_sequence, database):

    check_state(args.entry_point, origin_sequence)

    # Run origin sequence, and it continues until the game is done
    state = run_sequence(origin_sequence[args.entry_point], database)

    new_state = None

    while True:

        check_state(state, origin_sequence)

        new_state = run_sequence(origin_sequence[state], database)

        state = new_state


if __name__ == "__main__":

    execute_parse(origin_sequence, database)