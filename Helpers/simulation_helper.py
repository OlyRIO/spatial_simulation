from DTO.fly import *
from helpers.calculation_helper import CalculationHelper
from helpers.plot_helper import *
from helpers.data_generator_helper import *
from helpers.data_helper import *
from helpers.constant_helpers.simulation_constant_helper import *
from helpers.constant_helpers.directories_constant_helper import *
import pandas as pd
import numpy as np

class SimulationHelper:
    def __init__(self):
        calcHelper = CalculationHelper()
        
        self.stepNumber = STEP_NUMBER
        self.arenaRadius = ARENA_RADIUS_SCALED
        self.flyList = [Fly(calcHelper.generatePointInCircle()) for x in range(FLY_NUMBER)]
        self.distanceThreshold = INTERACTION_DISTANCE_THRESHHOLD
        
    def generateWalks(self):
        dataGenerator = DataGenerator()

        for fly in self.flyList:
            dataGenerator.generateRandomSteps(self.stepNumber)
            fly.moveInSequence(dataGenerator.steps)

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
        os.makedirs(MOVEMENT_DIR, exist_ok=True)
        os.makedirs(ANIMATION_DIR, exist_ok=True)
        os.makedirs(PLOT_DIR, exist_ok=True)
        
        animation_filename = ANIMATION_DIR + "/" + str(fly.id) + "_" + getCurrentTime()+ ".gif"
        plot_filename = PLOT_DIR + "/" + str(fly.id) + "_" + getCurrentTime() + ".png"
        movement_filename = MOVEMENT_DIR + "/" + str(fly.id) + "_" + getCurrentTime() + ".csv"
        
        df.to_csv(movement_filename)
        plotHelper.exportPlot(plot_filename)
        
        if (SHOULD_ANIMATE):
            plotHelper.exportAnimation(animation_filename)

    def exportAllFlyInteractions(self):
        flyDict = {fly.id: pd.DataFrame({"pos x": [point.x for point in fly.pointList],
                                      "pos y": [point.y for point in fly.pointList]})
               for fly in self.flyList}
        
        allFliesDistances = distances_between_all_flies(flyDict)
        allFliesInteractions = getFlyInteractions(allFliesDistances, self.distanceThreshold)
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        allFliesDistances.to_csv(OUTPUT_DIR + "/distances.csv", index = True)
        allFliesInteractions.to_csv(OUTPUT_DIR + "/interactions.csv", index = False)
        saveInteractionsAsGraph(allFliesInteractions)
