import math
from DTO.Point import *
from DTO.Step import *

class Fly:
    currentPosition = Point(0, 0)
    targetPoint = Point(0, 0)
    pointList = []

    def __init__(self, point):
        self.currentPosition = point
        self.pointList.append(point)

    def setTargetPos(self, step):
        targetX = step.distance * math.cos(step.direction)
        targetY = step.distance * math.sin(step.direction)
        self.targetPoint = Point(targetX, targetY)

    def move(self):
        if(self.currentPosition == self.targetPoint):
            return
        self.currentPosition = self.targetPoint
        self.pointList.append(self.currentPosition)
        

    def printAll(self):
        print("Current fly coordinates are ({}, {})" .format(self.x, self.y))