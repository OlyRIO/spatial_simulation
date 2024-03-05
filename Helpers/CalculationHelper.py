import random, math
from DTO.Point import *

class CalculationHelper:
    def __init__(self) -> None:
        pass

    """
    Generates a point inside of a bounding circle defined by the given radius and interval [0, 1].
    
        Args:
            circleRadius (float): Radius of the bounding circle.
            centerX (float): X coordinate of the center of the bounding circle.
            centerY (float): Y coordinate of the center of the bounding circle.
    
        Returns:
            float: a point with x and y coordinates between [0, 1] inside of a circle with a given radius.
        """
    def generatePointInCircle(self, circleRadius=0.5, centerX = 0.5, centerY=0.5):
        r = circleRadius * math.sqrt(random.random())
        theta = random.random() * 2 * math.pi
        x = centerX + r * math.cos(theta)
        y = centerY + r * math.sin(theta)

        return Point(x, y)

