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

        self.beta = beta
        self.sigma = sigma
        self.no_agents = n
        
        self.running =True # Necessary to run the model
        Human.create_agents(model=self, n=n)

        # Initializing the output file
        self.output_csv_path = f'{config.OUTPUT_DIR}/output.csv'
        with open(self.output_csv_path, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(config.OUTPUT_HEADERS)

    def write_csv_row(self):
        """ Calculates totals in each SIR compartment and adds a data row to csv """

        tick = int(self.time)
        tot_sus = sum(1 for a in self.agents if a.state == config.State.SUSCEPTIBLE)
        tot_inf = sum(1 for a in self.agents if a.state == config.State.INFECTED)
        tot_rec = sum(1 for a in self.agents if a.state == config.State.RECOVERED)

        with open(self.output_csv_path, mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tick, tot_sus, tot_inf, tot_rec])

    def infect_susceptible(self):
        """ Returns number of susceptible individuals who will be infected.
        The number is a drawn sample from a binomial distribution. """
        tot_sus = sum(1 for a in self.agents if a.state == config.State.SUSCEPTIBLE)
        no_chosen_agents = np.random.binomial(tot_sus, self.beta)

        # Pick random susceptible agents and change state
        susceptible = [agent for agent in self.agents if agent.state == config.State.SUSCEPTIBLE]

        chosen = self.random.sample(susceptible, no_chosen_agents)
        for agent in chosen:
            agent.state = config.State.INFECTED

    def recover_infected(self):
        """ Returns number of infected individuals who will recovered.
        The number is a drawn sample from a binomial distribution. """
        tot_inf = sum(1 for a in self.agents if a.state == config.State.INFECTED)
        no_inf_to_rec = np.random.binomial(tot_inf, self.sigma)

        return no_inf_to_rec

    def step(self):
        """ Advances the model by one step (one day) """

        self.infect_susceptible()
        self.agents.shuffle_do("step") # Reorders the list of agent objects
        self.write_csv_row()

if __name__ == "__main__":
    starter_model = DiseaseModel(n=1000, beta= 0.1, sigma=1, width=10, height=10)
    for _ in range(30):
        starter_model.step()
