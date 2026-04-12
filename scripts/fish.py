import numpy as np
from scripts import world_parameters

class Fish:
    def __init__(self, position_x, position_y):
        self.position_x,  self.position_y = position_x, position_y
        self.speed_x, self.speed_y = np.random.rand() - 0.5, np.random.rand() - 0.5
        self.color = (255, 0, 0)  # red color for the fish
        self.size = 5  # radius of the fish

    def update_position(self):
        self.position_x += self.speed_x
        self.position_y += self.speed_y