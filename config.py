# File to store project sertings

# Agent display settings
AGENT_SHAPE = "circle"
AGENT_RADIUS = 0.5
AGENT_FILL = "true"

# The keys relate to the integers representing the SIR compartments
# Refer to the class State
DICT_COLOR_AGENTS = {
    0: "green", # susceptible
    1: "red", # infected
    2: "yellow" # recovered
}

# Model settings
TOT_POP = 100 # total population
GRID_WIDTH = 10
GRID_HEIGHT = 10