import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Helpers.DataHelper import *
from Helpers.ConstantHelper import *

class PlotHelper:
    writer = animation.PillowWriter(fps=15,
                                metadata=dict(artist='Me'),
                                bitrate=300)
    
    def __init__(self):
        pass

    def setCoordinates(self, xCoords, yCoords):
        self.xCoords = np.array(xCoords)
        self.yCoords = np.array(yCoords)

    def exportPlot(self, filename, circleRadius = ARENA_RADIUS_SCALED):
        plt.figure()
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.tick_params(axis = 'both', length = 20)

        circle = plt.Circle((circleRadius, circleRadius), circleRadius, color='r', fill=False)
        ax.add_patch(circle)
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.plot(self.xCoords, self.yCoords)
        plt.savefig(filename)

        if (SHOULD_PLOT):
            plt.show()

    def exportAnimation(self, filename, circleRadius = ARENA_RADIUS_SCALED):
        fig = plt.figure()
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.tick_params(axis = 'both', length = 20)

        xdata, ydata = [], []
        line, = ax.plot([], [], lw=2)

        def data_gen():
            for i in range(len(self.xCoords)):
                yield self.xCoords[i], self.yCoords[i]

        def run(data):
            x, y = data
            xdata.append(x)
            ydata.append(y)

            line.set_data(xdata, ydata)

            return line

        def init():
            del xdata[:]
            del ydata[:]      
            line.set_data(xdata, ydata)

            return line

        circle = plt.Circle((circleRadius, circleRadius), circleRadius, color='r', fill=False)
        ax.add_patch(circle)
        plt.xlabel('X')
        plt.ylabel('Y')

        ani = animation.FuncAnimation(fig, run, data_gen, interval=50, init_func=init,
                              save_count = STEP_NUMBER)
        
        ani.save(filename, writer = self.writer)


