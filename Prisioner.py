import random
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid, MultiGrid
from mesa.datacollection import DataCollector
from mesa.visualization.ModularVisualization import VisualizationElement
from mesa.visualization.modules import CanvasGrid
import tkinter as tk

GRID_WIDTH = 800
GRID_HEIGHT = 800

PRISIONERS_PER_TYPE = 150

PRISIONERS_TYPES = {
    "AUTRUISTA": 1,  # não delata
    "EGOISTA": 2,  # sempre delata
}


class SlideButtonElement(VisualizationElement):
    package_includes = []
    local_includes = []

    def __init__(self, value):
        self.value = value

    def render(self):
        canvas = tk.Canvas(self)
        canvas.create_rectangle(0, 0, 100, 20, fill="gray")
        button_x = int(self.value * 100)
        canvas.create_oval(button_x - 5, 5, button_x + 5, 15, fill="red")
        return canvas


# Calcula a porcentagem de agentes que escolheram não delatar
def compute_autruista(model):
    agents_type = [agent.type for agent in model.schedule.agents]
    total_agents = len(agents_type)
    autruistas = 0
    for i in agents_type:
        if i == "AUTRUISTA":
            autruistas += 1
    return autruistas / total_agents


class PrisonerAgent(Agent):
    def __init__(self, unique_id, model, type):
        super().__init__(unique_id, model)
        self.jail_time = 0
        self.denounced_list = []
        self.type = type

    def step(self):
        self.move()
        self.snitch()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=True  # Verifica as diagonais
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def snitch(self):
        # Pega posições em volta
        adjacent_positions = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False  # Verifica as diagonais
        )

        # Retorna agentes próximos, em volta
        adjacent_agents = []
        for pos in adjacent_positions:
            x, y = pos
            if (
                0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT
            ):  # Verifica se a posição é válida na grade
                agent = self.model.grid[x][
                    y
                ]  # Obtém o agente na posição (x, y) da grade
                if agent:
                    adjacent_agents.extend(agent)

        if len(adjacent_agents) == 0:
            return

        best_jail_time = self.jail_time
        best_type = self.type

        for neighbor in adjacent_agents:
            if neighbor.jail_time < best_jail_time:
                best_type = neighbor.type
                best_jail_time = neighbor.jail_time

        # jail_time eh referente ao tempo de cadeida. Esta em anos
        if PRISIONERS_TYPES[self.type] == PRISIONERS_TYPES["EGOISTA"]:
            self.denounced_list.extend(adjacent_agents)
            for agent in adjacent_agents:
                if self in agent.denounced_list:
                    self.jail_time = self.jail_time + 5
                else:
                    self.jail_time = self.jail_time
        else:  # caso do comportamento ser AUTRUISTA
            for agent in adjacent_agents:
                if self in agent.denounced_list:
                    self.jail_time = self.jail_time + 10
                else:
                    self.jail_time = self.jail_time + 0.5

        if best_type != self.type:
            self.type = best_type


class PrisonerModel(Model):
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, False)
        self.running = True

        index = 0
        for type in PRISIONERS_TYPES:
            for _ in range(num_agents):
                a = PrisonerAgent(index, self, type)
                self.schedule.add(a)
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                self.grid.place_agent(a, (x, y))
                index += 1

        # Cria um coletor de dados
        self.datacollector = DataCollector(
            # Função que calcula a porcentagem de agentes que escolheram não delatar
            model_reporters={"Autruistas": compute_autruista}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def set_prisoners_per_type(self, value):
        global PRISIONERS_PER_TYPE
        PRISIONERS_PER_TYPE = value
