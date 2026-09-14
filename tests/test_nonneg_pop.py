import config
from config import DICT_TEST_PARAMS as dict
from model import DiseaseModel

import unittest

class TestNonNegativePopulation(unittest.TestCase):
    """ Test to ensure that none of the SIR populations are negative.
    Test is done over multiple time steps of the model as defined by n_model_steps.
    This test is especially important as the model gets more complex over time
    with birth, death rate and change in mechanics of movement of population across the compartments. """

    # Initializing objects and variables that will be used in each test
    def setUp(self):
        self.test_model = DiseaseModel(
            n=dict["tot_pop"], 
            beta= dict["beta"], 
            sigma= dict["sigma"], 
            no_initial_infc=dict["no_initial_infc"], 
            output_file_name=dict["output_file_name"]
        )

        self.n_model_steps = 10

    def test_susceptible_population(self):

        # Check for each time step (including day 0), the susceptible population is not negative
        for i in range(0, self.n_model_steps + 1):

            # Not progressing the model for step 0
            if i > 0:
                self.test_model.step()

            tot_sus = sum(1 for a in self.test_model.agents if a.state == config.State.SUSCEPTIBLE)
            self.assertGreaterEqual(tot_sus, 0)

    def test_infected_population(self):

        # Check for each time step (including day 0), the infected population is not negative
        for i in range(0, self.n_model_steps + 1):

            # Not progressing the model for step 0
            if i > 0:
                self.test_model.step()

            tot_infc = sum(1 for a in self.test_model.agents if a.state == config.State.INFECTED)
            self.assertGreaterEqual(tot_infc, 0)


    def test_recovered_population(self):

        # Check for each time step (including day 0), the recovered population is not negative
        for i in range(0, self.n_model_steps + 1):

            # Not progressing the model for step 0
            if i > 0:
                self.test_model.step()

            tot_rec = sum(1 for a in self.test_model.agents if a.state == config.State.RECOVERED)
            self.assertGreaterEqual(tot_rec, 0)
