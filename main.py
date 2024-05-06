from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGenerator import *
from Helpers.SimulationHelper import *
import pandas as pd

def main():
    simulation = SimulationHelper(flyNumber=5, stepNumber=700, stepSize=0.1, arenaRadius=0.5, distanceThreshold = 0.2, shouldPlot=False)
    simulation.generateWalks()
    simulation.exportAll()

    if simulation.shouldPlot:
        simulation.plotFlies()
        
    simulation.exportAllFlyInteractions()


if __name__=="__main__":
    main()