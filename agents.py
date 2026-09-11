from mesa import Agent

import config

# Creating a human agent with three states- susceptible, infected and
# recovered represented as booleans
class Human(Agent):
    def __init__(self, model):
        """ Initializes a Human instance"""
        Agent.__init__(self, model)

        # Initially all agents are susceptible
        self.state = config.State.SUSCEPTIBLE

        self.update_color()

    def susceptible_to_infected(self):
        """ Susceptible individuals become infected """
        if self.state == config.State.SUSCEPTIBLE:
            self.state = config.State.INFECTED
            print(f"Hi, I am  agent {self.unique_id!s} and I just got infected")


    def infected_to_recovered(self):
        """ Infected individuals recover """
        if self.state == config.State.INFECTED:
            self.state = config.State.RECOVERED
            print(f"Hi, I am  agent {self.unique_id!s} and I just recovered")

    def update_color(self):
        """ Updates agents' color based on which SIR compartment
        they belong to """

        self.color = config.DICT_COLOR_AGENTS[self.state]

    def step(self):
        """ The behavior of the agents in a single step of the model """
       
        self.susceptible_to_infected()
        self.infected_to_recovered()
        self.update_color()
        