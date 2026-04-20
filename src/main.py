import rich # for rich.print() to make printing look good
import random, time # basically just filler for arbitrary exec
import json # for handling parsing of json file containing the story line and game config
from sequence_parser import sequence_parse # for handling parsing the sequences


with open("config.json") as config_fp:
    raw_config_data = json.loads(config_fp.read())
config_data = dict(raw_config_data)

json_game_path = config_data["json_game_path"]
initial_entry_sequence = config_data["initial_entry_sequence"]

with open(json_game_path) as json_fp:
    raw_game_data = json.loads(json_fp.read())

game_sequences = dict(raw_game_data)

control_variables = dict()
data_variables = dict()

control_variables["game_end"] = False

sequence_parse(game_sequences, initial_entry_sequence, data_variables, control_variables)

