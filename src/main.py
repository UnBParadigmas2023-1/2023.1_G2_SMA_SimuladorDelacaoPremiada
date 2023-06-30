from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import random

class DelatorAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.informant = False
        self.cooperating_agents = []

    def step(self):
        if not self.informant:
            neighbors = self.model.grid.get_neighbors(self.pos, moore=False)
            cooperating_agents = [agent for agent in neighbors if isinstance(agent, DelatorAgent) and agent.informant]
            if cooperating_agents:
                self.cooperating_agents = cooperating_agents
                self.informant = random.choice(cooperating_agents)
                self.model.informant_agents.append(self)

class DelatorModel(Model):
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = RandomActivation(self)
        self.informant_agents = []
        self.running = True

        for i in range(self.num_agents):
            agent = DelatorAgent(i, self)
            self.schedule.add(agent)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"InformantAgents": lambda m: len(m.informant_agents)}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

        if len(self.informant_agents) == self.num_agents:
            self.running = False

# Configurações do modelo
num_agents = 100
width = 10
height = 10

# Criando o modelo
model = DelatorModel(num_agents, width, height)

# Executando a simulação
while model.running:
    model.step()

# Resultados
print("Número de agentes delatores:", len(model.informant_agents))
print(model.datacollector.get_model_vars_dataframe())
