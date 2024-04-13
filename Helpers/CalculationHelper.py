import random, math
from DTO.Point import *

class CalculationHelper:
    def __init__(self, circleRadius=0.5):
        self.circleRadius = circleRadius
        self.centerX = circleRadius
        self.centerY = circleRadius

    
    def generatePointInCircle(self):
        """
    Generates a point inside of a bounding circle defined by the given radius and interval [0, 1].
    
        Args:
            circleRadius (float): Radius of the bounding circle.
            centerX (float): X coordinate of the center of the bounding circle.
            centerY (float): Y coordinate of the center of the bounding circle.
    
        Returns:
            float: a point with x and y coordinates between [0, 1] inside of a circle with a given radius.
    """
        r = self.circleRadius * math.sqrt(random.random())
        theta = random.random() * 2 * math.pi
        x = self.centerX + r * math.cos(theta)
        y = self.centerY + r * math.sin(theta)

        return Point(x, y)
    
    def setCircle(self, circleRadius):
        self.circleRadius = circleRadius
        self.centerX = circleRadius
        self.centerY = circleRadius

    def isPointInCircle(self, point):
        """
    Checks if a point is inside of a circle
    
        Args:
            point (point): Point to be checked
            radius (float): Radius of the circle.
            centerX (float): X coordinate of the center of the bounding circle.
            centerY (float): Y coordinate of the center of the bounding circle.
    
        Returns:
            bool: is point inside of the circle
    """
        checkCondition = math.pow(point.x - self.centerX, 2) + math.pow(point.y - self.centerY, 2) < self.circleRadius * self.circleRadius 
        return checkCondition

