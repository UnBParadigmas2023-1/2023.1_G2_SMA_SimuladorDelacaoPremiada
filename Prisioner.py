import random
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid, MultiGrid

GRID_WIDTH = 30
GRID_HEIGHT = 30

PRISIONERS_PER_TYPE = 5

PRISIONERS_TYPES = {
    "AUTRUISTA": 1 , #não delata
    "EGOISTA": 2, #sempre delata
    "FLEXIVEL": 3, #depende da descisão do vizinho
}


class PrisonerAgent(Agent):
    def __init__(self, unique_id, model, type):
        super().__init__(unique_id, model)
        self.jail_time = random.randrange(1, 10)
        self.denounced_list = []
        self.type = type

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
        # Pega posições em volta
        adjacent_positions = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,  # Verifica as diagonais
            include_center=False)

        # Retorna agentes próximos, em volta
        adjacent_agents = []
        for pos in adjacent_positions:
            x, y = pos
            if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:  # Verifica se a posição é válida na grade
                agent = self.model.grid[x][y]  # Obtém o agente na posição (x, y) da grade
                if agent:
                    adjacent_agents.append(agent)

        if len(adjacent_agents) == 0:
            return
        
        best_jail_time = self.jail_time
        best_type = self.type
        best_neighbor = self.random.choice(adjacent_agents)[0]

        for neighbor_list in adjacent_agents:
            for neighbor in neighbor_list:
                if neighbor.jail_time < best_jail_time:
                    best_type = neighbor.type
                    best_jail_time = neighbor.jail_time
                    best_neighbor = neighbor

        if best_type != self.type:
            self.type = best_type

        # jail_time eh referente ao tempo de cadeida. Esta em anos
        if PRISIONERS_TYPES[self.type] == PRISIONERS_TYPES["EGOISTA"]:
            self.denounced_list.append(best_neighbor)
            if self in best_neighbor.denounced_list:
                self.jail_time = self.jail_time + 5
            else:
                self.jail_time = self.jail_time 
        elif PRISIONERS_TYPES[self.type] == PRISIONERS_TYPES["FLEXIVEL"]: # imita o melhor visinho
            if self in best_neighbor.denounced_list:
                self.denounced_list.append(best_neighbor)
                self.jail_time = self.jail_time + 5
            else:
                self.jail_time = self.jail_time + 0.5
        else: # caso do comportamento ser AUTRUISTA
            if self in best_neighbor.denounced_list:
                self.jail_time = self.jail_time + 10
            else:
                self.jail_time = self.jail_time + 0.5


class PrisonerModel(Model):
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, False)
        self.running = True
        
        index = 0
        for type in PRISIONERS_TYPES:
            for i in range(PRISIONERS_PER_TYPE): 
                a = PrisonerAgent(index, self, type) 
                self.schedule.add(a)
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                self.grid.place_agent(a, (x, y))
                index += 1

    def step(self):
        self.schedule.step() 
