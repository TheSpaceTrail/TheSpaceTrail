import rich

def sequence_parse(game_sequences, entry_sequence, data_variables, control_variables, return_sequence = None):
    
    """
    Handles parsing of individual sequences from a json game. 
    Any commands that jump to another sequence call this function recursively.
    This means the game has been exited in someway when the head function returns.
    """

    control_variables["game_end"] = False
    next_sequence = entry_sequence

    while not control_variables["game_end"]:

        sequence_items = game_sequences[next_sequence]

        current_sequence = next_sequence

        item_index = 0
        while item_index < len(sequence_items):
            
            item = sequence_items[item_index]

            print(item)

            if type(item) == type(""):
                item = item.strip()

            choice = ""

            # variable substition
            if item.find("$") >= 0:
                word_list: list[str] = item.split(" ")
                for word in range(len(word_list)):
                    if word_list[word][0] == "$":
                        word_list[word] = data_variables[word_list[word][1:].lower().strip()]

                item = " ".join(word_list)

            control_char = item[0]

            if control_char == "!": # this item must be a command
                
                command = item[1:]
                
                arguments = command.split(" ")
                command_type = arguments[0]
                print(command_type, arguments)

                match command_type:
                    case "store":

                        variable_name = arguments[1].lower().strip()
                        variable_data = arguments[2]
                        data_variables[variable_name] = variable_data
                        print(data_variables)
                        print(data_variables[variable_name])

                    case "jump_switch":
                        
                        switch_key = arguments[1].lower().strip()

                        switch_dict = sequence_items[item_index + 1] # big problem if this isn't a dictionary
                        item_index += 1 # so that it skips over the switch_dict on the next item 
                        assert type(switch_dict) == type({})

                        print(switch_dict)
                        print(switch_key)

                        switch_return = switch_dict[switch_key] # this the next sequence
                        
                        next_sequence = switch_return 
                        prev_sequence = current_sequence
                        break
                        

                    case "jump_if":

                        operand1 = int(arguments[1])
                        operand2 = int(arguments[2])
                        operation = arguments[3]
                        jump_sequence = arguments[4]

                        if operation == ">":
                            truth = operand1 > operand2
                        
                        elif operation == "<":
                            truth = operand1 < operand2

                        else:
                            truth = operand1 == operand2

                        if truth:
                            next_sequence = jump_sequence
                            prev_sequence = current_sequence
                            break

                    case "jump":
                        
                        jump_sequence = arguments[1]

                        next_sequence = jump_sequence
                        prev_sequence = current_sequence
                        break

                    case "end_sequence":
                        next_sequence = prev_sequence
                        break

                    case "end_game":
                        control_variables["game_end"] = True
                        break

                    case _: 
                        print("Command control character used but no valid command was found.")

            elif control_char == "?": # this item must be a question
                
                question = item[1:]
                
                options = sequence_items[item_index + 1]
                item_index += 1 # so that it skips over the options list on the next item 

                while True:

                    rich.print(question)
                    unchecked_choice = input().lower().strip()
                    
                    if unchecked_choice not in options:
                        continue
                    else:
                        choice = unchecked_choice
                        data_variables["choice"] = choice
                        break

            elif control_char == "*": # this item is arbitrary code execution, probably don't use this
                
                code = item[1:]
                exec(code)
                return

            else: # this item must be dialogue
                rich.print(item)

            item_index += 1 # move to the next item
            continue

        if next_sequence != current_sequence:
            break

    print("Game ended successfully")


    
