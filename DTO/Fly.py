import math
from DTO.Point import *
from DTO.Step import *
from Helpers.CalculationHelper import *

class Fly:
    currentPoint = Point(0, 0)
    targetPoint = Point(0, 0)
    pointList = []

    def __init__(self, point):
        self.currentPoint = point
        self.pointList.append(point)


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

    def moveTo(self, targetPoint):
        calcHelper = CalculationHelper()
        if (targetPoint == self.currentPoint or not calcHelper.isPointInCircle(targetPoint)):
            return
        
        self.currentPoint = targetPoint
        self.pointList.append(self.currentPoint)