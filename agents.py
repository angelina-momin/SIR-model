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

    def update_color(self):
        """ Updates agents' color based on which SIR compartment
        they belong to """

        self.color = config.DICT_COLOR_AGENTS[self.state]

    def step(self):
        """ The behavior of the agents in a single step of the model """

        self.update_color()
        