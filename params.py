from mesa.visualization.ModularVisualization import UserSettableParameter

GRID_SIZE = 50
GRID_X_SIZE = 800
GRID_Y_SIZE = 800

CANVAS_SIZE = 300

PRISIONERS_TYPES = {
    "ALTRUISTA": 1,  # não delata
    "EGOISTA": 2,  # sempre delata
}

SIMULATION_PARAMS = {
    "num_agents": UserSettableParameter(
        "slider",
        name="Quantidade de Agentes de cada tipo",
        value=200,
        min_value=100,
        max_value=300,
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