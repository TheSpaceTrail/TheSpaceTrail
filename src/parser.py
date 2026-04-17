

def sequence_parse(entry_sequence, return_sequence = None):
    
    assert control_variables in globals or control_variables in locals
    assert data_variables in globals or data_variables in locals

    item_index = 0
    while item_index < len(json_sequence):
        
        item: str = json_sequence[item_index].strip()

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
            exec_command(command, item_index)

        elif control_char == "?": # this item must be a question
            question = item[1:]
            exec_question(question, item_index)

        elif control_char == "*": # this item is arbitrary code execution
            code = item[1:]
            exec_code(code, item_index)

        item_index += 1


    
