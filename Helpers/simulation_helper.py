from DTO.fly import *
from helpers.calculation_helper import CalculationHelper
from helpers.plot_helper import *
from helpers.data_generator_helper import *
from helpers.data_helper import *
from helpers.constant_helpers.simulation_constant_helper import *
from helpers.constant_helpers.directories_constant_helper import *
import pandas as pd
import numpy as np

class SimulationHelper:
    def __init__(self):
        calc_helper = CalculationHelper()
        
        self.step_number = STEP_NUMBER
        self.arena_radius = ARENA_RADIUS_SCALED
        self.fly_list = [Fly(calc_helper.generate_point_in_circle()) for x in range(FLY_NUMBER)]
        self.distance_threshold = INTERACTION_DISTANCE_THRESHOLD
        
    def generate_walks(self):
        print("Generating walks...")
        dataGenerator = DataGenerator()

        for fly in self.fly_list:
            dataGenerator.generate_random_steps(self.step_number)
            fly.move_in_sequence(dataGenerator.steps)
        
        print("Walks generated.")

    def export_all(self):
        clear_all()

        for fly in self.fly_list:
            self.export_fly(fly)

    def animate_simulation(self):
        x_coordinates = [[point.x for point in fly.point_list] for fly in self.fly_list]
        y_coordinates = [[point.y for point in fly.point_list] for fly in self.fly_list]
        
        plot_helper = PlotHelper()
        plot_helper.set_coordinates(x_coordinates, y_coordinates)
        
        filename = ANIMATION_DIR + "/" + "all_flies" + "_" + get_current_time()+ ".gif"
        plot_helper.export_animation(filename, x_coordinates, y_coordinates)
        
                 
    def export_fly(self, fly):
        plot_helper = PlotHelper()
        x_coordinates = [point.x for point in fly.point_list]
        y_coordinates = [point.y for point in fly.point_list]

        plot_helper.set_coordinates(x_coordinates, y_coordinates)

        dict = {"id" : fly.id, "pos x": x_coordinates, "pos y": y_coordinates}
        df = pd.DataFrame(dict)
        os.makedirs(MOVEMENT_DIR, exist_ok=True)
        os.makedirs(ANIMATION_DIR, exist_ok=True)
        os.makedirs(PLOT_DIR, exist_ok=True)
        
        movement_filename = MOVEMENT_DIR + "/" + str(fly.id) + "_" + get_current_time() + ".csv"
        df.to_csv(movement_filename)
        
        plot_filename = PLOT_DIR + "/" + str(fly.id) + "_" + get_current_time() + ".png"
        plot_helper.export_plot(plot_filename)
            
    def export_all_fly_interactions(self):
        fly_dict = {fly.id: pd.DataFrame({"pos x": [point.x for point in fly.point_list],
                                      "pos y": [point.y for point in fly.point_list]})
               for fly in self.fly_list}
        
        all_flies_distances = distances_between_all_flies(fly_dict)
        all_flies_interactions = get_fly_interactions(all_flies_distances, self.distance_threshold)
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        all_flies_distances.to_csv(OUTPUT_DIR + "/distances.csv", index = True)
        all_flies_interactions.to_csv(OUTPUT_DIR + "/interactions.csv", index = False)
        save_as_graph(all_flies_interactions)
