import numpy as np
import DTO.Point
import matplotlib.pyplot as plt

class PlotHelper:
    def __init__(self):
        pass

    def setCoords(self, xCoords, yCoords):
        self.xCoords = np.array(xCoords)
        self.yCoords = np.array(yCoords)

    def plot(self, circleRadius=0.5):
        plt.figure()
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.tick_params(axis = 'both', length = 20)

        circle = plt.Circle((circleRadius, circleRadius), circleRadius, color='r', fill=False)
        ax.add_patch(circle)
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.plot(self.xCoords, self.yCoords)
        plt.show()

