import random
from DTO.Step import *
from Helpers.CalculationHelper import *

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
            dir = self.normalizeAngle(random.random())
            dist = random.uniform(0, stepSize)
            rndStep = Step(dir, dist)
            self.steps.append(rndStep)

    """
    Normalizes angle values from [0, 1] to [0, 2 * pi]

    Args:
            angle (float): angle to be normalized

    Returns:
            float: a normalized angle
    """
    def normalizeAngle(self, angle):
        return angle * 2 * math.pi