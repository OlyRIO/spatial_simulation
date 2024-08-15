class Step:
    """
    A class representing a step between two points

    ...
    Attributes
    ----------
    direction : float
        direction from the starting point to the ending point, measured in radians
    distance : float
        distance between the starting and ending point
    """

    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance