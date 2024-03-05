from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
import random


def main():
    calcHelper = CalculationHelper()
    points = [calcHelper.generatePointInCircle() for y in range(10)]
    xCoords = [point.x for point in points]
    yCoords = [point.y for point in points]
    print(xCoords)
    print("\n", yCoords)
    plotHelper = PlotHelper(xCoords, yCoords)
    plotHelper.plot()



if __name__=="__main__":
    main()