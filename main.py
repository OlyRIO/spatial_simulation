from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGenerator import *
import random
import numpy


def main():
    calcHelper = CalculationHelper()
    dataGenerator = DataGenerator(100)
    fly = Fly(calcHelper.generatePointInCircle())

    # Generate target points and move fly
    for step in dataGenerator.steps:
        targetPt = fly.getTargetPoint(step)
        fly.moveTo(targetPt)

    # Extract x and y coordinates
    xCoords, yCoords = zip(*[(point.x, point.y) for point in fly.pointList])

    # Plot the trajectory
    plotHelper = PlotHelper(xCoords, yCoords)
    plotHelper.plot()



if __name__=="__main__":
    main()