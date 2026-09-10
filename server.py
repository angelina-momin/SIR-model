from mesa.visualization.models import CanvasGrid

import config

def agent_portrayal(agent):
    portrayal = {
        "Shape": config.AGENT_SHAPE, 
        "Filled": config.AGENT_FILLED, 
        "r": config.AGENT_RADIUS,
        "Color": agent.color
        }

grid = CanvasGrid(agent_portrayal)
server = ModuleServer(DiseaseModel,
    [grid],
    "SIR Disease Model"
    {"N": config.TOT_POP,
    "width": config.MODEL_WIDTH.
    "height": config.MODEL_HEIGHT
    }
)

server.port = 8521
server.launch()