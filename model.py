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

        # Assuming only one individual is infected initially
        infc_agent = self.random.sample(list(self.agents), 1)[0]
        infc_agent.state = config.State.INFECTED

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

    def calculate_p_infc(self):
        tot_inf = sum(1 for a in self.agents if a.state == config.State.INFECTED)
        p =  1 - np.exp(- self.beta * tot_inf / self.no_agents)
        return p

    def infect_susceptible(self):
        """ Returns number of susceptible individuals who will be infected.
        The number is a drawn sample from a binomial distribution. """

        p_infc = self.calculate_p_infc()

        sus_agents = [agent for agent in self.agents if agent.state == config.State.SUSCEPTIBLE]
        
        no_sus_agents = len(sus_agents)
        no_chosen_agents = np.random.binomial(no_sus_agents, p_infc)

        # Pick random susceptible agents and change state
        chosen = self.random.sample(sus_agents, no_chosen_agents)
        for agent in chosen:
            agent.state = config.State.INFECTED

        # Keeping track of individuals who just became infected
        # They cannot recover in the same time step
        self.agents_just_infected = chosen

    def recover_infected(self):
        """ Returns number of infected individuals who will recovered.
        The number is a drawn sample from a binomial distribution. """

        inf_agents = [agent for agent in self.agents if agent.state == config.State.INFECTED and agent not in self.agents_just_infected]

        no_inf_agents = len(inf_agents)
        no_chosen_agents = np.random.binomial(no_inf_agents, self.sigma)

        chosen = self.random.sample(inf_agents, no_chosen_agents)
        for agent in chosen:
            agent.state = config.State.RECOVERED

    def step(self):
        """ Advances the model by one step (one day) """

        self.infect_susceptible()
        self.recover_infected()
        self.agents.shuffle_do("step") # Reorders the list of agent objects
        self.write_csv_row()

if __name__ == "__main__":
    starter_model = DiseaseModel(n=1000, beta= 10, sigma=1, width=10, height=10)
    for _ in range(10):
        starter_model.step()
