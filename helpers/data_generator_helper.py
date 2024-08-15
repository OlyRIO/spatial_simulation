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
        lowerLimit = 0
        upperLimit = 0
        currentDirection = 0
        
        if (not hasattr(self, 'steps')):
            self.steps = []
            
        if (len(self.steps) == 0):
            currentDirection = random.random()
        else:
             currentDirection = calc_helper.normalize_angle(self.steps[-1].direction)
       
        
        if (currentDirection - 0.125 < 0):
            lowerLimit = 1 - abs(currentDirection - 0.125)
        else:
            lowerLimit = currentDirection - 0.125
        
        if (currentDirection + 0.125 > 1):
            upperLimit = currentDirection + 0.125
        else:
            upperLimit = currentDirection + 0.125
        
        if (upperLimit < lowerLimit):
            temp = upperLimit
            upperLimit = lowerLimit
            lowerLimit = temp
        
        dir = calc_helper.angle_from_normalized(random.uniform(lowerLimit, upperLimit))
        dist = get_random_element_from_list(self.normalized_distances)
        
        return Step(dir, dist)