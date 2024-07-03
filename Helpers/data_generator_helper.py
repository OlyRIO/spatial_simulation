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
        self.normalized_distances = getDistancesData()
        
    def generateRandomSteps(self, stepNumber):
        """ Generates random steps
        Parameters:

        stepNumber (integer): Number of steps to be generated
        """

        self.steps = []
        calcHelper = CalculationHelper(ARENA_RADIUS_SCALED)
        
        for i in range(stepNumber):
            self.steps.append(self.generateRandomStep())

    def generateRandomStep(self):
        calcHelper = CalculationHelper(ARENA_RADIUS_SCALED)
        dir = calcHelper.normalizeAngle(random.random())
        dist = getRandomElementFromList(self.normalized_distances)
        
        return Step(dir, dist)