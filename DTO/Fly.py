import math
from DTO.Point import *

class Fly:
    currentPosition = Point(0, 0)
    orientation = 0
    targetPoint = Point(0, 0)

    def __init__(self, point):
        self.x = point.x
        self.y = point.y

    def setOrientation(self, orientation):
        self.orientation = orientation

    def setTargetPos(self, stepLength):
        targetX = stepLength * math.cos(self.orientation)
        targetY = stepLength * math.sin(self.orientation)
        self.targetPoint = Point(targetX, targetY)

    def move(self, frequency = 1/12):
        deltaX = self.x - self.targetPoint.x
        deltaY = self.y - self.targetPoint.y
        self.currentPosition.x += self.targetPoint.x * frequency
        self.currentPosition.y += self.targetPoint.y * frequency
        

    def printAll(self):
        print("Current fly coordinates are ({}, {})" .format(self.x, self.y))