import math
from DTO.Point import *
from DTO.Step import *
from Helpers.CalculationHelper import *
from Helpers.DataGeneratorHelper import *
import itertools

class Fly:
    id_iterator = itertools.count(start=1)

    def __init__(self, point):
        self.currentPoint = point
        self.pointList = [point]
        self.id = next(self.id_iterator)

    """
    Moves the current point of the fly by the given step

        Args:
            step (step): Step containing the direction and orientation to move to the new point
    
        Returns:
            point: new position of the fly
    
    """
    def getTargetPoint(self, step):
        targetX = step.distance * math.cos(step.direction)
        targetY = step.distance * math.sin(step.direction)

        return Point(self.currentPoint.x + targetX, self.currentPoint.y + targetY)

    def moveInSequence(self, stepList):
        calcHelper = CalculationHelper()
        dataGenerator = DataGenerator()

        for step in stepList:
            targetPoint = self.getTargetPoint(step)

            while targetPoint == self.currentPoint or not calcHelper.isPointInCircle(targetPoint):
                targetPoint = self.getTargetPoint(dataGenerator.generateRandomStep())

            self.moveTo(targetPoint)

    def moveTo(self, targetPoint):
        self.currentPoint = targetPoint
        self.pointList.append(self.currentPoint)