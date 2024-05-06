from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGenerator import *
from Helpers.DataUtilityHelper import *
import pandas as pd
import numpy as np
import os
import glob
import time
from pathlib import Path

class SimulationHelper:
    def __init__(self, flyNumber, stepNumber, stepSize = 0.1, arenaRadius = 0.5, distanceThreshold = 0.2, shouldPlot = False):
        calcHelper = CalculationHelper(arenaRadius)
        
        self.shouldPlot = shouldPlot
        self.stepNumber = stepNumber
        self.stepSize = stepSize
        self.arenaRadius = arenaRadius
        self.flyList = [Fly(calcHelper.generatePointInCircle()) for x in range(flyNumber)]
        self.distanceThreshold = distanceThreshold
        
    def generateWalks(self):
        dataGen = DataGenerator()

        for fly in self.flyList:
            dataGen.generateRndSteps(self.stepNumber, self.stepSize)
            fly.moveInSequence(dataGen.steps, self.arenaRadius)

    def plotFlies(self):
        plotHelper = PlotHelper()
        
        for fly in self.flyList:
            xCoords, yCoords = zip(*[(point.x, point.y) for point in fly.pointList])
            plotHelper.setCoords(xCoords, yCoords)
            plotHelper.plot(self.arenaRadius)

    def exportAll(self):
        self.clearData()

        counter = 1
        for fly in self.flyList:
            self.exportFly(fly, counter)
            counter +=1

    def exportFly(self, fly, id):
        xCoords = [point.x for point in fly.pointList]
        yCoords = [point.y for point in fly.pointList]
        dict = {"id" : fly.id, "pos x": xCoords, "pos y": yCoords}
        df = pd.DataFrame(dict)

        df.to_csv(self.getDataDirectory() + "/" + str(fly.id) + "_" + self.getCurrTime() + ".csv")

    def exportAllFlyInteractions(self):
        flyDict = {fly.id: pd.DataFrame({"pos x": [point.x for point in fly.pointList],
                                      "pos y": [point.y for point in fly.pointList]})
               for fly in self.flyList}
        
        allFliesDistances = distances_between_all_flies(flyDict)
        allFliesDistances.to_csv(self.getDataDirectory() + "/distances.csv", index=True)
        allFliesInteractions = getFlyInteractions(allFliesDistances, self.distanceThreshold)
        allFliesInteractions.to_csv(self.getDataDirectory() + "/interactions.csv", index=False)


    def clearData(self):
        self.clearDirectory(self.getDataDirectory())

    def getDataDirectory(self):
        path = Path(os.getcwd())

        return str(path) + "/Data"

    def clearDirectory(self, directory_path):
        try:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("All files deleted successfully.")
        except OSError:
            print("Error occurred while deleting files. Try closing all files first.")

    def getCurrTime(self):
        t = time.localtime
        current_time = time.strftime('%Y-%m-%d--%H-%M-%S')
        return current_time
