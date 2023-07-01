from Prisioner import PrisonerModel, GRID_WIDTH, GRID_HEIGHT
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 1}

    if agent.is_informer:
        portrayal["Color"] = "red"
    else:
        portrayal["Color"] = "blue"

    portrayal["Layer"] = 0

    return portrayal


grid = CanvasGrid(agent_portrayal, GRID_WIDTH, GRID_HEIGHT, 600, 600)

server = ModularServer(
    PrisonerModel,
    [grid],
    "Prisioner Model",
    {"num_agents": 10, "width": 30, "height": 30},
)
server.port = 8521
server.launch()
