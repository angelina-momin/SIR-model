from mesa import Model

from agents import Human

class DiseaseModel(Model):
    """ Environment in which the human agents live and transmit diseases"""
    def __init__(self, n, width, height):
        super().__init__(rng=rng)
        self.no_agents = n

        # Creating grid where the agents can move
        self.grid = MultiGrid(width, height, True)

        Human.create_agents(model=self, n)

    def step(self):
        """ Advances the model by one step (one day) """

        self.agents.shuffle_do("step")
