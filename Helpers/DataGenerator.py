import random
from DTO.Step import *

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
    steps = []

    def __init__(self, stepNumber):
        self.generateRndSteps(stepNumber)
        
    def generateRndSteps(self, stepNumber):
        for i in range(stepNumber):
            dir = random.random()
            dist = random.random()
            rndStep = Step(dir, dist)
            self.steps.append(rndStep)