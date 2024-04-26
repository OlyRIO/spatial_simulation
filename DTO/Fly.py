import math
from DTO.Point import *
from DTO.Step import *
from Helpers.CalculationHelper import *
import itertools

class Fly:
    id_iter = itertools.count(start=1)

    def __init__(self, point):
        self.currentPoint = point
        self.pointList = [point]
        self.id = next(self.id_iter)

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

    def moveInSequence(self, stepList, circleRadius = 0.5):
        for step in stepList:
            targetPt = self.getTargetPoint(step)

            self.moveTo(targetPt, circleRadius)

    def moveTo(self, targetPoint, circleRadius = 0.5):
        calcHelper = CalculationHelper(circleRadius)

        if (targetPoint == self.currentPoint or not calcHelper.isPointInCircle(targetPoint)):
            self.pointList.append(self.currentPoint)
            return
        
        self.currentPoint = targetPoint
        self.pointList.append(self.currentPoint)