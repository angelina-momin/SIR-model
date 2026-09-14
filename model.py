import csv
import os

from mesa import Model
import numpy as np

from agents import Human
import config

class DiseaseModel(Model):
    """ Environment in which the human agents live and transmit diseases"""
    def __init__(self, n, beta, sigma, no_initial_infc=1, output_file_name = "output.csv", rng=None):
        super().__init__(rng=rng)

        self.beta = beta
        self.sigma = sigma
        self.no_agents = n
        
        self.running =True # Necessary to run the model
        Human.create_agents(model=self, n=n)

        # Creating initial number of infections in random agents
        chosen_sus_agent_list = self.random.sample(population=list(self.agents), k=no_initial_infc)

        for sus_agent in chosen_sus_agent_list:
            sus_agent.state = config.State.INFECTED

        # Initializing the output file
        self.output_csv_path = f'{config.OUTPUT_DIR}{output_file_name}.csv'

        # Create the output dir if it does not exist
        if not os.path.exists(config.OUTPUT_DIR):
            os.makedirs(config.OUTPUT_DIR)

        # Adding headers and data for first day to csv
        with open(self.output_csv_path, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(config.OUTPUT_HEADERS)

        self.write_csv_row()
            
    def write_csv_row(self):
        """ Calculates totals in each SIR compartment and adds a data row to csv file """

        tick = int(self.time)
        tot_sus = sum(1 for a in self.agents if a.state == config.State.SUSCEPTIBLE)
        tot_inf = sum(1 for a in self.agents if a.state == config.State.INFECTED)
        tot_rec = sum(1 for a in self.agents if a.state == config.State.RECOVERED)

        with open(self.output_csv_path, mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tick, tot_sus, tot_inf, tot_rec])

    def calculate_p_si(self):
        """ Calculates the probability of a susceptible human becoming infected"""
        tot_inf = sum(1 for a in self.agents if a.state == config.State.INFECTED)
        p_si =  1 - np.exp(- self.beta * tot_inf / self.no_agents)
        return p_si

    def infect_susceptible(self):
        """ Returns number of susceptible individuals who will be infected.
        The number is a drawn sample from a binomial distribution. """

        p_infc = self.calculate_p_si()

        sus_agents = [agent for agent in self.agents if agent.state == config.State.SUSCEPTIBLE]
        
        no_sus_agents = len(sus_agents)

        # Determing the number of susceptible agents to infect
        no_chosen_agents = np.random.binomial(n=no_sus_agents, p=p_infc)

        # Pick random susceptible agents and change state
        chosen = self.random.sample(population=sus_agents, k=no_chosen_agents)
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

        # Determing the number of infected agents to recover
        no_chosen_agents = np.random.binomial(n=no_inf_agents, p=self.sigma)

        chosen = self.random.sample(population=inf_agents, k=no_chosen_agents)
        for agent in chosen:
            agent.state = config.State.RECOVERED

    def step(self):
        """ Advances the model by one step (one day) """

        self.infect_susceptible()
        self.recover_infected()
        self.agents.shuffle_do("step") # Reorders the list of agent objects
        self.write_csv_row()
