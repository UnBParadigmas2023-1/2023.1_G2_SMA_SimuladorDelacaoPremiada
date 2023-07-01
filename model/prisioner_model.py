import random
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class PrisonerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.strategy = random.choice(["C", "N"])
        self.time_served = 0

    def play(self):
        return self.strategy

    def update_strategy(self, opponent_strategy):
        if self.strategy == "C" and opponent_strategy == "C":
            self.time_served += 5
        elif self.strategy == "C" and opponent_strategy == "N":
            self.time_served += 0
        elif self.strategy == "N" and opponent_strategy == "C":
            self.time_served += 10
        elif self.strategy == "N" and opponent_strategy == "N":
            self.time_served += 0.6

class PrisonerModel(Model):
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(1, 1, False)

        for i in range(self.num_agents):
            a = PrisonerAgent(i, self)
            self.schedule.add(a)
            x = self.grid.width // 2
            y = self.grid.height // 2
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()
        self.play_round()
        self.update_time_served()

    def play_round(self):
        agents = self.schedule.agents
        for a in agents:
            opponent = random.choice(agents)
            opponent_strategy = opponent.play()
            a.update_strategy(opponent_strategy)
            self.update_time_served_per_round(a, opponent)

    def update_time_served(self):
        agents = self.schedule.agents
        for a in agents:
            a.time_served += 1