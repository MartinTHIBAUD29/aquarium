import numpy as np
from scripts import world_parameters, fish

class Aquarium():
    def __init__(self):
        self.fishes = [fish.Fish(np.random.rand() * world_parameters.SCREEN_WIDTH, np.random.rand() * world_parameters.SCREEN_HEIGHT)
                                for _ in range(world_parameters.NUMBER_OF_FISH)]

    def update_fishes_position(self):
        for fish in self.fishes:
            fish.update_position()
