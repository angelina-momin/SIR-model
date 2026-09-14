import config
from config import DICT_TEST_PARAMS as dict
from model import DiseaseModel

import unittest

class TestNonNegativePopulation(unittest.TestCase):
    """ Test to ensure that none of the SIR populations are negative.
    This is especially important as the model gets more complex over time
    with birth, death rate and change in mechanics of movement of population across the compartments. """

    test_model = DiseaseModel(
        n=dict["tot_pop"], 
        beta= dict["beta"], 
        sigma= dict["sigma"], 
        no_initial_infc=dict["no_initial_infc"], 
        output_file_name=dict["output_file_name"]
    )

    n_model_steps = 10

    def test_susceptible_population(self, test_model, n_model_steps):

        # Check for number of steps that the susceptible population is always >= 0
        for step in range(n_model_steps + 1):
            test_model.step()
            tot_sus = sum(1 for a in self.agents if a.state == config.State.SUSCEPTIBLE)
            self.assertGreaterEqual(tot_sus, 0)

    # def test_infected_population(self, n_model_steps):

    # def test_recovered_population(self):

