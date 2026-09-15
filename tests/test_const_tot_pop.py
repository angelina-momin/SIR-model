import config
from src.model import DiseaseModel

import unittest

class TestConstantTotPop(unittest.TestCase):
    """ Test to ensure that the sum of populations in SIR compartments remains constant 
    and equal to total population"""

    # Initializing objects and variables that will be used in each test
    def setUp(self):
        self.test_model = DiseaseModel(
            tot_pop=5000, 
            beta= 1, 
            sigma=1, 
            no_initial_infc=10, 
            output_file_name="test_tot_pop"
        )

        self.n_model_steps = 30

    def test_constant_tot_population(self):

        # Check for each time step (including day 0), the susceptible population is not negative
        for i in range(0, self.n_model_steps + 1):

            # Not progressing the model for step 0
            if i > 0:
                self.test_model.step()

            tot_sus = sum(1 for a in self.test_model.agents if a.state == config.State.SUSCEPTIBLE)
            tot_inf = sum(1 for a in self.test_model.agents if a.state == config.State.INFECTED)
            tot_rec = sum(1 for a in self.test_model.agents if a.state == config.State.RECOVERED)

            sum_pop_sir = tot_sus + tot_inf + tot_rec

            self.assertEqual(sum_pop_sir, self.test_model.tot_pop)
