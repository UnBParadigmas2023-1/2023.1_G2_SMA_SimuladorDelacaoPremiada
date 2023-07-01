import random
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid, MultiGrid

GRID_WIDTH = 30
GRID_HEIGHT = 30

def prisioner_dillema():
    probability = 0.5
    return random.random() < probability


class PrisonerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.jail_time = 5
        self.is_informer = False
        self.denounced_list = []

    def step(self):
        self.move()
        self.snitch()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,  # Verifica as diagonais
            include_center=True)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def snitch(self):
        adjacent_positions = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,  # Verifica as diagonais
            include_center=False)

        adjacent_agents = []
        for pos in adjacent_positions:
            x, y = pos
            if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:  # Verifica se a posição é válida na grade
                agent = self.model.grid[x][y]  # Obtém o agente na posição (x, y) da grade
                if agent:
                    adjacent_agents.append(agent[0])

        if adjacent_agents:
            neighbor = self.random.choice(adjacent_agents)

            should_snitch = prisioner_dillema()
            if should_snitch:
                self.is_informer = True
                self.denounced_list.append(neighbor)
                if self in neighbor.denounced_list:
                    self.jail_time = self.jail_time/2
                else:
                    self.jail_time -= 1
            else:
                if self in neighbor.denounced_list:
                    self.jail_time = self.jail_time*2


class PrisonerModel(Model):
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, False)
        self.running = True

        for i in range(self.num_agents):
            a = PrisonerAgent(i, self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()
