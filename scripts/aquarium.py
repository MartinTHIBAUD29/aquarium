import numpy as np
from scripts import world_parameters, fish

class Aquarium():
    def __init__(self):
        self.fish1 = fish.Fish(np.array([500, 400]))

    def update_fishes_position(self):
        return
