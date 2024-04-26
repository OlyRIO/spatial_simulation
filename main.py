from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGenerator import *
from Helpers.SimulationHelper import *

def main():
    simulation = SimulationHelper(flyNumber=5, stepNumber=700, stepSize=0.1, arenaRadius=0.5, shouldPlot=True)
    simulation.generateWalks()
    simulation.exportAll()
    # simulation.plotFlies()
    simulation.exportAllFlyInteractions()
    

if __name__=="__main__":
    main()