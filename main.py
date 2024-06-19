from DTO.Fly import *
from Helpers.CalculationHelper import CalculationHelper
from Helpers.PlotHelper import *
from Helpers.DataGeneratorHelper import *
from Helpers.SimulationHelper import *
from Helpers.ConstantHelper import *
import pandas as pd

def main():
    simulation = SimulationHelper()
    simulation.generateWalks()
    simulation.exportAll()
    simulation.exportAllFlyInteractions()  


if __name__=="__main__":
    main()