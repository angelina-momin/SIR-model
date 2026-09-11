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
    State.SUSCEPTIBLE: "green", 
    State.INFECTED: "red",
    State.RECOVERED: "yellow" 
}

# Model settings
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Output dir
OUTPUT_DIR = "data/"
OUTPUT_HEADERS = ["tick", "tot_sus", "tot_inf", "tot_rec"]