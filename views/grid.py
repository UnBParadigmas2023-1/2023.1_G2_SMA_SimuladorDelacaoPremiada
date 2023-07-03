from mesa.visualization.modules import CanvasGrid
from views.portrayal import agent_portrayal
from params import GRID_SIZE, GRID_X_SIZE, GRID_Y_SIZE

grid = CanvasGrid(agent_portrayal, GRID_SIZE, GRID_SIZE, GRID_X_SIZE, GRID_Y_SIZE)