import json
import time
import re
import os
import sys

import rich
import rich.text

from pyfiglet import Figlet

from . import terminal

MIN_WIDTH = 130
MIN_HEIGHT = 35

PAUSE_GAME_LOOP = False
LETTER_SPEED_MULTIPLIER = 5

os.system("rem") # Init the terminal

rich_console = rich.get_console()
tstt = terminal.terminal(rich_console, letter_speed_multiplier=LETTER_SPEED_MULTIPLIER)

rich_console.show_cursor(False)

def init():

    os.system("cls")

    tstt.force_window_size(MIN_HEIGHT, MIN_WIDTH)

    tstt.slowprint("Location\n[green]Earth[/green]\nYear\n[purple]2069[/purple]", letters_per_second=10)

    tstt.print("Press enter to start...", end=False)

    sys.stdin.readline()

    tstt.clear_screen()

    tstt.print(Figlet().renderText("The Space Trail"), center_vertically=True)

    time.sleep(10)

if __name__ == '__main__':
    
    init()

