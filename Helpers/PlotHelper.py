import numpy as np
import DTO.Point
import matplotlib.pyplot as plt

class PlotHelper:
    def __init__(self, xCoords, yCoords):
        self.xCoords = np.array(xCoords)
        self.yCoords = np.array(yCoords)

    def plot(self, circleRadius=0.5, centerX=0.5, centerY=0.5, plotPoints = True):
        plt.figure()
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.tick_params(axis = 'both', length = 20)

        circle = plt.Circle((centerX, centerY), circleRadius, color='r', fill=False)
        ax.add_patch(circle)
        plt.xlabel('X')
        plt.ylabel('Y')

        if (plotPoints):
            plt.plot(self.xCoords, self.yCoords)

        plt.show()

