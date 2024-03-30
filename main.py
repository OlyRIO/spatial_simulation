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

    for step in dataGenerator.steps:
        targetPt = fly.getTargetPoint(step)
        fly.moveTo(targetPt)

    xCoords = [point.x for point in fly.pointList]
    yCoords = [point.y for point in fly.pointList]
    plotHelper = PlotHelper(xCoords, yCoords)

    plotHelper.plot()



if __name__=="__main__":
    main()