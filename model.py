from mesa import Model

from agents import Human

class DiseaseModel(Model):
    def __init__(self, n):
        super().__init__(rng=rng)
        self.num_agents = num_agents

        Human.create_agents(model=self, n)

    def step(self):
        """ Advances the model by one step (one day) """

        self.agents.shuffle_do("step")
        