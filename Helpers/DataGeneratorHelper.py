import random
from DTO.Step import *
from Helpers.CalculationHelper import *
from Helpers.DataUtilityHelper import *
from Helpers.ConstantHelper import *

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
        pass
        
    def generateRndSteps(self, stepNumber, stepSize):
        self.steps = []
        
        for i in range(stepNumber):
            calcHelper = CalculationHelper(ARENA_RADIUS)

            dir = calcHelper.normalizeAngle(random.random())
            dist = random.uniform(0, stepSize)
            rndStep = Step(dir, dist)
            self.steps.append(rndStep)