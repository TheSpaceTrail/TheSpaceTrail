Planning:
- Problem Statment: A Game based off The Oregon Trail (https://oregontrail.ws/games/the-oregon-trail/)
- Must make storyboard and write dialogue
    - Goal is to get to Saturn
    - Pick a country to join
    - Purchase resources before leaving
    - Start your journey
    - You will face obstacles along the way such as pirates, food shortages, asteroid fields, and other countries with the same goal

- Implement storyboard and dialogue
    - Design architecture of system

- Create title.py with Turtle
    - A rocketship in space; main screen


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
        - modify value sign amount: add arms or food or other values to the player object
        - end: ends the game unconditionally
        - if variable operator value: check if some value exceeds or is lower than some other value and jump to section if so
        - shop: Instantiates shop object based on JSON object and runs it
        - number sign: comment, like python
        - ?: runs rich prompt to ask for user input and jumps to sequence or sets choice value pased on the type of the following object
        - random hop: jump to one of a selection, equally weighted


Notes:
- Our main decision was to make a custom language in order to facilitate the coding process and make it easier
- We learned that making a custom Domain-Specific language based on JSON is not an efficient or effective way to program a video game.
- It is hard to maintain and takes much longer than just using the Python language directly

Testing:
- All questions should have their input verified with the list that comes after.

- Shop test (run `python -m src.shop`) --> should function correctly --> it does

- !random_hop a b --> should jump randomly (50/50) between sequence a and be --> it does

- !if parts >= 1 --> should go to sequence 1 when false --> it does

- !jump moon --> should start moon sequence by accesing it from top level of story line --> works

- printing with formatting e.g. "[red]Code 418[/red] --> should print it in red, removing any tags --> prints perfectly to console

- ? queried e.g. ?Do you help them? --> prints "Do you help them?" and opens prompt for the user to answer, when the prompt is incorrect it asks again --> works


Reflection:
- It would have taken much less time to write the game in a normal way. 
- In the future I would recommend to write this in a normal way.

