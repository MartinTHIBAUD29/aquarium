import numpy as np
from scripts import world_parameters

class Fish:
    def __init__(self, position):
        self.position = position

    def update_position(self):
        return