import random
from DTO.step import *
from helpers.calculation_helper import *
from helpers.data_helper import *
from helpers.constant_helpers.simulation_constant_helper import *

class DataGenerator:
    """
    A class used to generate random testing data during development

    ...

    Attributes
    ----------
    step : List<step>
        a list of step objects used to calculate a series of next points

    Methods
    -------
    generateRndSteps(stepNumber)
        generates a number of random steps equal to stepNumber
    """

    def __init__(self):
        self.normalized_distances = get_distances_data()
        
    def generate_random_steps(self, stepNumber):
        """ Generates random steps
        Parameters:

        stepNumber (integer): Number of steps to be generated
        """

        self.steps = []
        calc_helper = CalculationHelper()
        
        for i in range(stepNumber):
            self.steps.append(self.generate_random_step())

    def generate_random_step(self):
        calc_helper = CalculationHelper()
        dir = calc_helper.normalize_angle(random.random())
        dist = get_random_element_from_list(self.normalized_distances)
        
        return Step(dir, dist)