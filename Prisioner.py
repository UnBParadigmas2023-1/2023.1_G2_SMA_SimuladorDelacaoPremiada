import random
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import MultiGrid


class PrisonerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=False, include_center=True
        )

        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)


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
