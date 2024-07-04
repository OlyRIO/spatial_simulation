import random, math
from DTO.point import *
from helpers.constant_helpers.simulation_constant_helper import *

class CalculationHelper:
    def __init__(self, circle_radius = ARENA_RADIUS_SCALED):
        self.circle_radius = circle_radius
        self.center_x = circle_radius
        self.center_y = circle_radius

    
    def generate_point_in_circle(self):
        """
    Generates a point inside of a bounding circle defined by the given radius and interval [0, 1].
    
        Args:
            circle_radius (float): Radius of the bounding circle.
            center_x (float): X coordinate of the center of the bounding circle.
            center_y (float): Y coordinate of the center of the bounding circle.
    
        Returns:
            float: a point with x and y coordinates between [0, 1] inside of a circle with a given radius.
    """
        
        r = self.circle_radius * math.sqrt(random.random())
        theta = random.random() * 2 * math.pi
        x = self.center_x + r * math.cos(theta)
        y = self.center_y + r * math.sin(theta)

        return Point(x, y)
    
    def set_circle(self, circle_radius):
        self.circle_radius = circle_radius
        self.center_x = circle_radius
        self.center_y = circle_radius

    def is_point_in_circle(self, point):
        """
        Checks if a point is inside of a circle
    
        Args:
            point (point): Point to be checked
            radius (float): Radius of the circle.
            center_x (float): X coordinate of the center of the bounding circle.
            center_y (float): Y coordinate of the center of the bounding circle.
    
        Returns:
            bool: is point inside of the circle
    """
        
        check_condition = math.pow(point.x - self.center_x, 2) + math.pow(point.y - self.center_y, 2) \
        < self.circle_radius * self.circle_radius 

        return check_condition
    
    def normalize_angle(self, angle):
        """
    Normalizes angle values from [0, 1] to [0, 2 * pi]

    Args:
            angle (float): angle to be normalized

    Returns:
            float: a normalized angle
    """
        
        return angle * 2 * math.pi

