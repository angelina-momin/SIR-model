from enum import Enum

# File to store project settings

class State(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2

# Agent display settings
AGENT_SHAPE = "circle"
AGENT_RADIUS = 0.5
AGENT_FILL = "true"

# Agent display color based on compartments
DICT_COLOR_AGENTS = {
    State.SUSCEPTIBLE: "blue", 
    State.INFECTED: "orange",
    State.RECOVERED: "green" 
}

# Output dir
OUTPUT_DIR = "data/"
OUTPUT_HEADERS = ["tick", "tot_sus", "tot_inf", "tot_rec"]