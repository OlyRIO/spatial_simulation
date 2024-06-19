from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGeneratorHelper import *
from Helpers.DataUtilityHelper import *
from Helpers.DataUtilityHelper import *
from Helpers.ConstantHelper import *
import pandas as pd
import numpy as np
import glob

class SimulationHelper:
    def __init__(self):
        calcHelper = CalculationHelper(ARENA_RADIUS)
        
        self.stepNumber = STEP_NUMBER
        self.stepSize = STEP_SIZE
        self.arenaRadius = ARENA_RADIUS
        self.flyList = [Fly(calcHelper.generatePointInCircle()) for x in range(FLY_NUMBER)]
        self.distanceThreshold = DISTANCE_THRESHHOLD
        
    def generateWalks(self):
        dataGen = DataGenerator()

        for fly in self.flyList:
            dataGen.generateRndSteps(self.stepNumber, self.stepSize)
            fly.moveInSequence(dataGen.steps, self.arenaRadius)

    def exportAll(self):
        clearAll()

        for fly in self.flyList:
            self.exportFly(fly)

    def exportFly(self, fly):
        plotHelper = PlotHelper()
        xCoords = [point.x for point in fly.pointList]
        yCoords = [point.y for point in fly.pointList]

        plotHelper.setCoords(xCoords, yCoords)

        dict = {"id" : fly.id, "pos x": xCoords, "pos y": yCoords}
        df = pd.DataFrame(dict)
        animation_filename = getAnimationDirectory() + "/" + str(fly.id) + "_" + getCurrentTime()+ ".gif"
        plot_filename = getPlotDirectory() + "/" + str(fly.id) + "_" + getCurrentTime() + ".png"
        
        df.to_csv(getDataDirectory() + "/" + str(fly.id) + "_" + getCurrentTime() + ".csv")
        plotHelper.exportAnimation(animation_filename)
        plotHelper.exportPlot(plot_filename)

    def exportAllFlyInteractions(self):
        flyDict = {fly.id: pd.DataFrame({"pos x": [point.x for point in fly.pointList],
                                      "pos y": [point.y for point in fly.pointList]})
               for fly in self.flyList}
        
        allFliesDistances = distances_between_all_flies(flyDict)
        allFliesDistances.to_csv(getDataDirectory() + "/distances.csv", index=True)
        allFliesInteractions = getFlyInteractions(allFliesDistances, self.distanceThreshold)
        allFliesInteractions.to_csv(getDataDirectory() + "/interactions.csv", index=False)
