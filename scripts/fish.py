import numpy as np
from scripts import world_parameters

class Fish:
    def __init__(self, position):
        self.position_x, self.position_y = position

    def update_position(self):
        self.position_x += np.random.rand() - 0.5
        self.position_y += np.random.rand() - 0.5