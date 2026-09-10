from mesa import Model
from mesa import MultiGrid

from agents import Human

class DiseaseModel(Model):
    """ Environment in which the human agents live and transmit diseases"""
    def __init__(self, n, width, height):
        super().__init__(rng=rng)
        self.no_agents = n

        # Creating grid where the agents can move
        self.grid = MultiGrid(width, height, True)

        # Creating agents 
        for i in range(self.no_agents):
            human = Human(i, self)

            # Place agent in random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(human, (x, y))

    def step(self):
        """ Advances the model by one step (one day) """

        self.agents.shuffle_do("step")
