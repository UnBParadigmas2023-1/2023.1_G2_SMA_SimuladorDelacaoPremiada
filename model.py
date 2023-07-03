from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from agent import PrisonerAgent
from params import PRISIONERS_TYPES


# Calcula a porcentagem de agentes que escolheram não delatar
def compute_altruista(model):
    agents_type = [agent.type for agent in model.schedule.agents]
    total_agents = len(agents_type)
    altruistas = 0
    for i in agents_type:
        if i == "ALTRUISTA":
            altruistas += 1
    return altruistas / total_agents

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
            model_reporters={"Altruistas": compute_altruista}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def set_prisoners_per_type(self, value):
        global PRISIONERS_PER_TYPE
        PRISIONERS_PER_TYPE = value