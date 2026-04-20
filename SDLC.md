Planning:
- Game will be based off The Oregon Trail (https://oregontrail.ws/games/the-oregon-trail/)
- Must make storyboard and write dialogue
    - Goal is to get to Saturn
    - Pick a country to join
    - Purchase resources before leaving
    - Start your journey
    - You will face obstacles along the way such as pirates, food shortages, asteroid fields, and other countries with the same goal
- Implement storyboard and dialogue
    - Design architecture of system
- Create title.py with Turtle
    - A rocketship in space


Design:
- Put dialogue and storyline into a json file and then build a parser to generate the gameplay loop
    - The json file is a dictionary of game sequences of dialogue and choices
    - each sequence is structured as name_of_sequence: [list of dialogue and choices]
    - the default type of values within the list is a dialogue string
    - formatted as "dialogue [color]stuff[/color]", will be printed using rich so formatting from that can be directly used within dialogue and choices

    - all other types of values such as commands or questions will be denoted by starting with a control character

    - all questions will start with ? i.e. "?what choice do you want?"
    - questions must be followed by a list of options such as [option1, option2, option3]
    - within the scope of the sequence and up until the next question, the result of the question will be stored as a variable named choice

    - all commands will start with ! i.e. "!store country $choice"
    - putting a dollar sign before a name will interpret that name as a preexisting variable and will substitute in it's value
    - command reference:
        - store variable_name value: stores the value in a variable with the identifier variable_name, can later be referenced using $variable_name
        - jump_switch switch_key, {case1: sequence1, ...}: must be followed by a dictionary, takes the switch argument and uses it as a key for the dictionary, then jumps to the sequence name matching the case
        - jump_if operand1 operand2 operation sequence: compares operand1 and operand2 using operation then jumps to sequence if the condition evaluates to true. Supported operations are =, <, and >, defaults to =. 
        - jump sequence: jumps to the specified sequence
        - end_sequence: goes back to the previous sequence unconditionally
        - end_game: ends the game unconditionally
        
    - all arbitrary python code execution can be done by starting a sequence item with "*"
    - the string following the "*" must be valid executable python code 
    - such as "*print("Hello, World!")

