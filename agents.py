from mesa import Agent

# Creating a human agent with three states- susceptible, infected and
# recovered represented as booleans
class Human(Agent):
    def __init__(self, model):
        """ Initializes a Human instance"""
        Agent.__init__(self, model)

        # Initially are susceptible
        self.susceptible = 1
        self.infected = 0 
        self.recovered = 0

    def move(self):
        """ Move the agent to a random neighboring cell """
        self.cell = self.cell.neighborhood.select_random_cell()

    def susceptible_to_infected(self):
        """ Susceptible individuals become infected """


    def infected_to_recovered(self):
        """ Infected individuals recover """

        

    def update_color(self):
        """ Updates agents' color based on which SIR compartment
        they belong to """

    def step(self):
        """ The behavior of the agents in a single step of the model """
       
        self.move()
        self.susceptible_to_infected()
        self.infected_to_recovered()
        self.update_color()
        