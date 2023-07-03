from mesa import Agent
from params import GRID_X_SIZE, GRID_Y_SIZE, PRISIONERS_TYPES


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
                0 <= x < GRID_X_SIZE and 0 <= y < GRID_Y_SIZE
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
        else:  # caso do comportamento ser AlTRUISTA
            for agent in adjacent_agents:
                if self in agent.denounced_list:
                    self.jail_time = self.jail_time + 10
                else:
                    self.jail_time = self.jail_time + 0.5

        if best_type != self.type:
            self.type = best_type