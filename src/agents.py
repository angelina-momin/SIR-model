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

        # Boolean to check whether the agent was infected today
        # Used to ensure the same agent does not recover in the same time stamp
        self.infected_today = False 

        self.update_color()

    def update_color(self):
        """ Updates agents' color based on which SIR compartment
        they belong to """

        self.color = config.DICT_COLOR_AGENTS[self.state]

    def step(self):
        """ The behavior of the agents in a single step of the model """

        self.update_color()
        # Infected today is set to False for the end of the day as we move to the next day
        self.infected_today = False
        