from DTO.fly import *
from helpers.calculation_helper import CalculationHelper
from helpers.plot_helper import *
from helpers.data_generator_helper import *
from helpers.simulation_helper import *
from helpers.constant_helpers.simulation_constant_helper import *
from helpers.data_helper import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import stats

def main():
    simulation = SimulationHelper()
    
    simulation.generateWalks()
    simulation.exportAll()
    simulation.exportAllFlyInteractions()  
    exportGraphGlobalMeasures()
    
if __name__=="__main__":
    main()  