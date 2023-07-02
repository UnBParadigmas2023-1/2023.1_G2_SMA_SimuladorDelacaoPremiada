from Prisioner import (
    PrisonerModel,
    PRISIONERS_TYPES,
)
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa import Model, Agent
from mesa.visualization.ModularVisualization import UserSettableParameter

GRID_SIZE = 50
GRID_X_SIZE = 800
GRID_Y_SIZE = 800
CANVAS_SIZE = 300


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 1}

    if PRISIONERS_TYPES[agent.type] == PRISIONERS_TYPES["AUTRUISTA"]:
        portrayal["Color"] = "green"
    elif PRISIONERS_TYPES[agent.type] == PRISIONERS_TYPES["EGOISTA"]:
        portrayal["Color"] = "red"

    portrayal["Layer"] = 0

    return portrayal


SIMULATION_PARAMS = {
    "num_agents": UserSettableParameter(
        "slider",
        name="Quantidade de Agentes Vivos",
        value=200,
        min_value=50,
        max_value=200,
        step=1,
        description="",
    ),
    "width": UserSettableParameter(
        "slider",
        name="Largura do quadro",
        value=GRID_SIZE,
        min_value=GRID_SIZE - 30,
        max_value=GRID_SIZE,
        step=1,
        description="",
    ),
    "height": UserSettableParameter(
        "slider",
        name="Comprimento do quadro",
        value=GRID_SIZE,
        min_value=GRID_SIZE - 30,
        max_value=GRID_SIZE,
        step=1,
        description="",
    ),
}


grid = CanvasGrid(agent_portrayal, GRID_SIZE, GRID_SIZE, GRID_X_SIZE, GRID_Y_SIZE)

chart = ChartModule(
    [{"Label": "Autruistas", "Color": "Black"}],
    data_collector_name="datacollector",
)

server = ModularServer(
    PrisonerModel,
    [grid, chart],
    "Prisioner Model",
    SIMULATION_PARAMS,
)

server.port = 8521
server.launch()
