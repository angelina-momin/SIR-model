import csv

from mesa import Model
from mesa.discrete_space import OrthogonalMooreGrid 
# from mesa.time import RandomActivation
import numpy as np

from agents import Human
import config

class DiseaseModel(Model):
    """ Environment in which the human agents live and transmit diseases"""
    def __init__(self, n, beta, sigma, width, height, rng=None):
        super().__init__(rng=rng)
        self.no_agents = n
        # self.schedule = RandomActivation(self) # Random selection of agents
        
        self.running =True # Necessary to run the model
        Human.create_agents(model=self, n=n)

        # Initializing the output file
        self.output_csv_path = f'{config.OUTPUT_DIR}/output.csv'
        with open(self.output_csv_path, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(config.OUTPUT_HEADERS)

        # # Creating grid where the agents can move
        # self.grid = OrthogonalMooreGrid((width, height))

        # # Creating agents 
        # for i in range(self.no_agents):
        #     human = Human(i, self)

        #     # Place agent in random grid cell
        #     x = self.random.randrange(self.grid.width)
        #     y = self.random.randrange(self.grid.height)
        #     self.grid.place_agent(human, (x, y))

    def write_csv_row(self):
        """ Calculates totals in each SIR compartment and adds a data row to csv """

        tick = int(self.time)
        tot_sus = sum(1 for a in self.agents if a.state == config.State.SUSCEPTIBLE)
        tot_inf = sum(1 for a in self.agents if a.state == config.State.INFECTED)
        tot_rec = sum(1 for a in self.agents if a.state == config.State.RECOVERED)

        with open(self.output_csv_path, mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tick, tot_sus, tot_inf, tot_rec])

    def draw_num_sus_to_infect(self):
        """ Returns number of susceptible individuals who will be infected.
        The number is a drawn sample from a binomial distribution. """
        tot_sus = sum(1 for a in self.agents if a.state == config.State.SUSCEPTIBLE)
        no_sus_to_inf = np.random.binomial(tot_sus, self.beta)

        return no_sus_to_inf

    def draw_num_inf_to_recover(self):
        """ Returns number of infected individuals who will recovered.
        The number is a drawn sample from a binomial distribution. """
        tot_inf = sum(1 for a in self.agents if a.state == config.State.INFECTED)
        no_inf_to_rec = np.random.binomial(tot_inf, self.sigma)

        return no_inf_to_rec

    def step(self):
        """ Advances the model by one step (one day) """

        self.agents.shuffle_do("step") # Reorders the list of agent objects
        self.write_csv_row()

if __name__ == "__main__":
    starter_model = DiseaseModel(n=1000, beta= 10, sigma=1, width=10, height=10)
    starter_model.step()
    starter_model.step()
    starter_model.step()
