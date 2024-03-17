from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
import random


def main():
    calcHelper = CalculationHelper()
    points = [calcHelper.generatePointInCircle() for y in range(20)]
    xCoords = [point.x for point in points]
    yCoords = [point.y for point in points]
    plotHelper = PlotHelper(xCoords, yCoords)
    plotHelper.plot()



if __name__=="__main__":
    main()