from model import PrisonerModel
from views.chart import chart
from views.grid import grid
from params import SIMULATION_PARAMS
from mesa.visualization.ModularVisualization import ModularServer


server = ModularServer(
    PrisonerModel,
    [grid, chart],
    "Prisioner Model",
    SIMULATION_PARAMS,
)

server.port = 8521
server.launch()
