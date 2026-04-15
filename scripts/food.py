from scripts import world_parameters

class Food():
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.range_of_detection = world_parameters.FOOD_RANGE_OF_DETECTION

    