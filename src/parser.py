import rich

def sequence_parse(json_file_pointer, entry_sequence, return_sequence = None):
    
    assert control_variables in globals or control_variables in locals
    assert data_variables in globals or data_variables in locals

    json_sequence = json_file[entry_sequence]

    current_sequence = entry_sequence

    item_index = 0
    while item_index < len(json_sequence):
        
        item = json_sequence[item_index]

        if type(item) == type(""):
            item = item.strip()

        choice = ""

        # variable substition
        if item.find("$") >= 0:
            word_list: list[str] = item.split(" ")
            for word in range(len(word_list)):
                if word_list[word][0] == "$":
                    word_list[word] = data_variables[word_list[word][1:]]

            item = "".join(word_list)

        control_char = item[0]

        if control_char == "!": # this item must be a command
            
            command = item[1:]
            
            arguments = command.split(" ")
            command_type = arguments[0]

            match command_type:
                case "store":

                    variable_name = arguments[1]
                    variable_data = arguments[2]
                    data_variables[variable_name] = variable_data

                case "jump_switch":
                    
                    switch_key = arguments[1]

                    switch_dict = json_sequence[item_index + 1] # big problem if this isn't a dictionary
                    assert type(switch_dict) == type({})

                    switch_return = switch_dict[switch_key]

                    sequence_parse(json_file_pointer, switch_return)

                case "jump_if":

                    operand1 = arguments[1]
                    operand2 = arguments[2]
                    operation = arguments[3]
                    jump_sequence = arguments[4]

                    if operation == ">":
                        truth = operand1 > operand2
                    
                    elif operation == "<":
                        truth = operand1 < operand2

                    else:
                        truth = operand1 == operand2

                    sequence_parse(json_file_pointer, jump_sequence, current_sequence)

                case "jump":
                    
                    jump_sequence = arguments[1]

                    sequence_parse(json_file_pointer, jump_sequence, current_sequence)

                case "end":
                    sequence_parse(json_file_pointer, return_sequence, current_sequence)

        elif control_char == "?": # this item must be a question
            
            question = item[1:]
            
            options = json_sequence[item_index + 1]

            while True:

                rich.print(question)
                unchecked_choice = input()
                
                if unchecked_choice not in options:
                    continue
                else:
                    choice = unchecked_choice
                    break

        elif control_char == "*": # this item is arbitrary code execution, probably don't use this
            
            code = item[1:]
            exec(code)
            return

        else: # this item must be dialogue
            rich.print(item)

        item_index += 1 # move to the next item
        continue

    
