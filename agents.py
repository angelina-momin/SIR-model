from mesa import Agent

# Creating a human agent with three states- susceptible, infected and
# recovered represented as booleans
class Human(Agent):
    def __init__(self, model):
        Agent.__init__(self, model)

        # Initially are susceptible
        self.susceptible = 1
        self.infected = 0 
        self.recovered = 0

    # Do they move? If so, create new function
    
        