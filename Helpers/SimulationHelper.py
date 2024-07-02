from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGeneratorHelper import *
from Helpers.DataHelper import *
from Helpers.ConstantHelper import *
import pandas as pd
import numpy as np
import glob

class SimulationHelper:
    def __init__(self):
        calcHelper = CalculationHelper(ARENA_RADIUS_SCALED)
        
        self.stepNumber = STEP_NUMBER
        self.arenaRadius = ARENA_RADIUS_SCALED
        self.flyList = [Fly(calcHelper.generatePointInCircle()) for x in range(FLY_NUMBER)]
        self.distanceThreshold = INTERACTION_DISTANCE_THRESHHOLD
        
    def generateWalks(self):
        dataGenerator = DataGenerator()

        for fly in self.flyList:
            dataGenerator.generateRandomSteps(self.stepNumber)
            fly.moveInSequence(dataGenerator.steps, self.arenaRadius)

    def exportAll(self):
        clearAll()

        for fly in self.flyList:
            self.exportFly(fly)

    def exportFly(self, fly):
        plotHelper = PlotHelper()
        xCoordinates = [point.x for point in fly.pointList]
        yCoordinates = [point.y for point in fly.pointList]

        plotHelper.setCoordinates(xCoordinates, yCoordinates)

        dict = {"id" : fly.id, "pos x": xCoordinates, "pos y": yCoordinates}
        df = pd.DataFrame(dict)
        animation_filename = getAnimationDirectory() + "/" + str(fly.id) + "_" + getCurrentTime()+ ".gif"
        plot_filename = getPlotDirectory() + "/" + str(fly.id) + "_" + getCurrentTime() + ".png"
        
        df.to_csv(getOutputDirectory() + "/" + str(fly.id) + "_" + getCurrentTime() + ".csv")

        if (SHOULD_ANIMATE):
            plotHelper.exportAnimation(animation_filename)

        plotHelper.exportPlot(plot_filename)

    def exportAllFlyInteractions(self):
        flyDict = {fly.id: pd.DataFrame({"pos x": [point.x for point in fly.pointList],
                                      "pos y": [point.y for point in fly.pointList]})
               for fly in self.flyList}
        
        allFliesDistances = distances_between_all_flies(flyDict)
        allFliesDistances.to_csv(getOutputDirectory() + "/distances.csv", index = True)
        allFliesInteractions = getFlyInteractions(allFliesDistances, self.distanceThreshold)
        allFliesInteractions.to_csv(getOutputDirectory() + "/interactions.csv", index = False)
