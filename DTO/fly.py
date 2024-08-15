import math
from DTO.point import *
from DTO.step import *
from helpers.calculation_helper import *
from helpers.data_generator_helper import *
import itertools

class Fly:
    id_iterator = itertools.count(start=1)

    def __init__(self, point):
        self.current_point = point
        self.point_list = [point]
        self.id = next(self.id_iterator)

    """
    Moves the current point of the fly by the given step

        Args:
            step (step): Step containing the direction and orientation to move to the new point
    
        Returns:
            point: new position of the fly
    
    """
    def get_target_point(self, step):
        target_x = step.distance * math.cos(step.direction)
        target_y = step.distance * math.sin(step.direction)

        return Point(self.current_point.x + target_x, self.current_point.y + target_y)

    def move_in_sequence(self, step_list):
        calc_helper = CalculationHelper()
        data_generator = DataGenerator()

        for step in step_list:
            target_point = self.get_target_point(step)

            while target_point == self.current_point or not calc_helper.is_point_in_circle(target_point):
                tempDirection = calc_helper.normalize_angle(step.direction)
                tempDirection = tempDirection + 0.25
                if (tempDirection > 1):
                    tempDirection = tempDirection - 1
                    
                step.direction = calc_helper.angle_from_normalized(tempDirection)
                target_point = self.get_target_point(step)
            self.move_to(target_point)

    def move_to(self, target_point):
        self.current_point = target_point
        self.point_list.append(self.current_point)