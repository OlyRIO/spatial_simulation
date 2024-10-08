import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation
from helpers.data_helper import *
from helpers.constant_helpers.simulation_constant_helper import *
from helpers.constant_helpers.directories_constant_helper import *

class PlotHelper:
    writer = animation.PillowWriter(fps=15,
                                metadata=dict(artist='Me'),
                                bitrate=300)
    
    def __init__(self):
        pass

    def set_coordinates(self, xCoords, yCoords):
        self.xCoords = np.array(xCoords)
        self.yCoords = np.array(yCoords)

    def export_plot(self, filename, circleRadius = ARENA_RADIUS_SCALED):
        if (not EXPORT_STATIC and not PLOT_STATIC):
            return
        
        plt.figure()
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.tick_params(axis = 'both', length = 20)

        circle = plt.Circle((circleRadius, circleRadius), circleRadius, color='r', fill=False)
        ax.add_patch(circle)
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.plot(self.xCoords, self.yCoords)
        
        if (PLOT_STATIC):
            plt.show()
                
        if (EXPORT_STATIC):
            plt.savefig(filename)
            
        plt.close()

    def export_animation(self, filename, all_x_coords, all_y_coords, circleRadius = ARENA_RADIUS_SCALED):
        if (not EXPORT_ANIMATION and not PLOT_ANIMATION):
            return
        
        start_time = time.time()
        fig = plt.figure()
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.tick_params(axis = 'both', length = 20)

        lines = [ax.plot([], [], marker='o')[0] for _ in range(STEP_NUMBER)]
        
        def init():
            for line in lines:
                line.set_data([], [])
            return lines

        circle = plt.Circle((circleRadius, circleRadius), circleRadius, color='r', fill=False)
        ax.add_patch(circle)
        plt.xlabel('X')
        plt.ylabel('Y')
        
        def update(frame):
            for line, x_coords, y_coords in zip(lines, all_x_coords, all_y_coords):
                if frame < len(x_coords):
                    start_index = max(0, frame - 4)  # Ensure we don't go below zero
                    line.set_data(x_coords[start_index:frame+1], y_coords[start_index:frame+1])
            return lines

        # Call the animator
        anim = animation.FuncAnimation(fig, update, frames=STEP_NUMBER, init_func=init, blit=True, interval=500)
        
        if(EXPORT_ANIMATION):
            anim.save(filename, writer = self.writer)
            end_time = time.time()
            print("Time elapsed for all flies animation: {}" .format(end_time - start_time))
            
        if(PLOT_ANIMATION):
            plt.show()
        
    def plot_measures(self):
        TREATMENTS = ["CsCh", "pseudo_CsCh", "RWN"]
        all_treatments = load_files_from_directory(TREATMENTS_DIR, file_format=".csv")
        all_treatments = {key: value for key, value in all_treatments.items() if key.replace(".csv", "") in TREATMENTS}

        os.makedirs(MEASURES_DIR, exist_ok=True)

        dataframes = []
        for treatment_name, treatment_path in all_treatments.items():
            treatment_name = treatment_name.replace(".csv", "")
            if treatment_name in TREATMENTS:
                df = pd.read_csv(treatment_path, index_col=0)
                df["Treatment"] = treatment_name
                dataframes.append(df)

        combined_data = pd.concat(dataframes)
        combined_data_reset = combined_data.reset_index()
        for measure_name in combined_data.columns.tolist():
            if measure_name == "Treatment":
                continue

            treatment_sums = {}
            for treatment in TREATMENTS:
                treatment_sums[f"sum_{treatment}"] = combined_data_reset[combined_data_reset["Treatment"] == treatment][
                    measure_name
                ]

            group_labels = []
            for treatment in TREATMENTS:
                group_labels.extend(
                    [treatment] * len(combined_data_reset[combined_data_reset["Treatment"] == treatment][measure_name])
                )

            if combined_data_reset[measure_name].min() == combined_data_reset[measure_name].max():
                continue

            fig, axes = plt.subplots()
            plt.suptitle(f"Distribution of {measure_name}", fontsize=10)

            sns.boxplot(
                data=combined_data_reset,
                x="Treatment",
                y=measure_name,
                dodge=False,
                hue="Treatment",
                ax=axes,
            )

            axes.set_xlabel("Treatment")
            axes.set_ylabel(measure_name)
            axes.tick_params(rotation=90)
            axes.set_ylim(0, combined_data_reset[measure_name].max() * 1.1)
            fig.autofmt_xdate()
            
            save_path = os.path.join(MEASURES_DIR, f"{measure_name}.png")
            plt.savefig(save_path)


