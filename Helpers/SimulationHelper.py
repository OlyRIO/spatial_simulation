from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGenerator import *

class SimulationHelper:
    def __init__(self, flyNumber, stepNumber, stepSize = 0.1, arenaRadius = 0.5, shouldPlot = False):
        calcHelper = CalculationHelper(arenaRadius)
        
        self.stepNumber = stepNumber
        self.stepSize = stepSize
        self.arenaRadius = arenaRadius
        self.flyList = [Fly(calcHelper.generatePointInCircle()) for x in range(flyNumber)]

        # self.generateWalks()

        # if(shouldPlot):
        #     self.plotFlies()            
        
    def generateWalks(self):
        dataGen = DataGenerator()

        for fly in self.flyList:
            dataGen.generateRndSteps(self.stepNumber, self.stepSize)
            fly.moveInSequence(dataGen.steps, self.arenaRadius)

    def plotFlies(self):
        for fly in self.flyList:
            xCoords, yCoords = zip(*[(point.x, point.y) for point in fly.pointList])
            plotHelper = PlotHelper(xCoords, yCoords)
            plotHelper.plot(self.arenaRadius, self.arenaRadius, self.arenaRadius)

