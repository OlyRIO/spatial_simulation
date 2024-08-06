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
    
    simulation.generate_walks()
    simulation.export_all()
    simulation.animate_simulation()
    simulation.export_all_fly_interactions()  
    
    # export_all_graphs_global_measures()

if __name__=="__main__":
    plot_helper = PlotHelper()
    
    for i in range(1000):
        main()
        
    export_all_graphs_global_measures()
    plot_helper.plot_measures()