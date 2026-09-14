from enum import Enum

# File to store project parameters

class State(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2

# Agent display color based on compartments
DICT_COLOR_AGENTS = {
    State.SUSCEPTIBLE: "blue", 
    State.INFECTED: "orange",
    State.RECOVERED: "green" 
}

# Output dir
OUTPUT_DIR = "data/"
OUTPUT_HEADERS = ["tick", "tot_sus", "tot_inf", "tot_rec"]

# Model parameters for unittests
DICT_TEST_PARAMS = {
    "tot_pop": 1000,
    "beta": 10,
    "sigma": 1,
    "no_initial_infc": 1,
    "output_file_name": "test"
}