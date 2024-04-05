from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGenerator import *
from Helpers.SimulationHelper import *
import random
import numpy


def main():
    simulation = SimulationHelper(flyNumber=1, stepNumber=700, stepSize=0.1, shouldPlot=True)
    simulation.generateWalks()
    simulation.plotFlies()



if __name__=="__main__":
    main()