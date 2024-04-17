from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGenerator import *
import pandas as pd
import os
import glob
import time
from pathlib import Path

class SimulationHelper:
    def __init__(self, flyNumber, stepNumber, stepSize = 0.1, arenaRadius = 0.5, shouldPlot = False):
        calcHelper = CalculationHelper(arenaRadius)
        
        self.stepNumber = stepNumber
        self.stepSize = stepSize
        self.arenaRadius = arenaRadius
        self.flyList = [Fly(calcHelper.generatePointInCircle()) for x in range(flyNumber)]
        
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

        df.to_csv(self.getDataDirectory() + "/" + str(fly.id) + "_" + self.getCurrTime())

    def clearData(self):
        self.clearDirectory(self.getDataDirectory())

    def getDataDirectory(self):
        path = Path(os.getcwd())
        # parentDir = path.parent.absolute()

        return str(path) + "\\Data"

    def clearDirectory(self, directory_path):
        try:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("All files deleted successfully.")
        except OSError:
            print("Error occurred while deleting files.")

    def getCurrTime(self):
        t = time.localtime
        current_time = time.strftime('%Y-%m-%d--%H-%M-%S')
        return current_time
