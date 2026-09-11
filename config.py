# File to store project sertings

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
TOT_POP = 100 # total population
GRID_WIDTH = 10
GRID_HEIGHT = 10