from Prisioner import PrisonerModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 1}
    portrayal["Color"] = "red"
    portrayal["Layer"] = 0

    return portrayal


grid = CanvasGrid(agent_portrayal, 30, 30, 600, 600)

server = ModularServer(
    PrisonerModel,
    [grid],
    "Prisioner Model",
    {"num_agents": 100, "width": 30, "height": 30},
)
server.port = 8521
server.launch()
