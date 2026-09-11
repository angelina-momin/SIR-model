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

    def change_state(self):
        """ Susceptible individuals become infected """
        if self.state == config.State.SUSCEPTIBLE:
            self.state = config.State.INFECTED
            print(f"Hi, I am  agent {self.unique_id!s} and I just got infected")

        elif self.state == config.State.INFECTED:
            self.state = config.State.RECOVERED
            print(f"Hi, I am  agent {self.unique_id!s} and I just recovered")

    def update_color(self):
        """ Updates agents' color based on which SIR compartment
        they belong to """

        self.color = config.DICT_COLOR_AGENTS[self.state]

    def step(self):
        """ The behavior of the agents in a single step of the model """

        print(f"Hi, I am  agent {self.unique_id!s}")
        self.change_state()
        self.update_color()
        print(f"My state is {self.state} and my color {self.color}")


        