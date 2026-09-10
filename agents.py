from enum import Enum
from mesa import Agent

import config 

class State(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2

# Creating a human agent with three states- susceptible, infected and
# recovered represented as booleans
class Human(Agent):
    def __init__(self, model, state):
        """ Initializes a Human instance"""
        Agent.__init__(self, model)

        # Initially all agents are susceptible
        self.state = State.SUSCEPTIBLE

        self.update_color()

    def move(self):
        """ Move the agent to a random neighboring cell """
        self.cell = self.cell.neighborhood.select_random_cell()

    def susceptible_to_infected(self):
        """ Susceptible individuals become infected """
        if self.state = State.SUSCEPTIBLE:
            self.state = State.INFECTED


    def infected_to_recovered(self):
        """ Infected individuals recover """
        if self.state = State.INFECTED:
            self.state = State.RECOVERED

    def update_color(self):
        """ Updates agents' color based on which SIR compartment
        they belong to """

        self.color = DICT_COLOR_AGENTS[self.state]

    def step(self):
        """ The behavior of the agents in a single step of the model """
       
        self.move()
        self.susceptible_to_infected()
        self.infected_to_recovered()
        self.update_color()
        