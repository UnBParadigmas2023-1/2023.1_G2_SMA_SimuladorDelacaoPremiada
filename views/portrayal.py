from model import PrisonerModel
from params import PRISIONERS_TYPES

def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 1}

    if PRISIONERS_TYPES[agent.type] == PRISIONERS_TYPES["ALTRUISTA"]:
        portrayal["Color"] = "green"
    elif PRISIONERS_TYPES[agent.type] == PRISIONERS_TYPES["EGOISTA"]:
        portrayal["Color"] = "red"

    portrayal["Layer"] = 0

    return portrayal
