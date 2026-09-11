from mesa import Model
from mesa.discrete_space import OrthogonalMooreGrid 
# from mesa.time import RandomActivation

from agents import Human

class DiseaseModel(Model):
    """ Environment in which the human agents live and transmit diseases"""
    def __init__(self, n, width, height, rng=None):
        super().__init__(rng=rng)
        self.no_agents = n
        # self.schedule = RandomActivation(self) # Random selection of agents
        
        self.running =True # Necessary to run the model
        Human.create_agents(model=self, n=n)
        # # Creating grid where the agents can move
        # self.grid = OrthogonalMooreGrid((width, height))

        # # Creating agents 
        # for i in range(self.no_agents):
        #     human = Human(i, self)

        #     # Place agent in random grid cell
        #     x = self.random.randrange(self.grid.width)
        #     y = self.random.randrange(self.grid.height)
        #     self.grid.place_agent(human, (x, y))

    def step(self):
        """ Advances the model by one step (one day) """

        self.agents.shuffle_do("step")

if __name__ == "__main__":
    starter_model = DiseaseModel(n=2, width=10, height=10)
    starter_model.step()
