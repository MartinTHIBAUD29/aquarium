import numpy as np
from scripts import world_parameters, fish

class Aquarium():
    def __init__(self):
        self.fishes = []
        for i in range(world_parameters.NUMBER_OF_FISH):
            fish_position_x = np.random.rand() * world_parameters.SCREEN_WIDTH
            fish_position_y = np.random.rand() * world_parameters.SCREEN_HEIGHT
            self.fishes.append(fish.Fish(i, fish_position_x, fish_position_y))

    def update_fishes_neighborhood(self):        
        for fish in self.fishes: 
            fish.neighbors = []
            for other in self.fishes:
                if fish.distance_to(other) < fish.field_of_view:
                    fish.neighbors.append(other.identification)
     
    def update_fishes_position(self):
        self.update_fishes_neighborhood()
        for fish in self.fishes:
            fish.update_position()

    def create_new_fish(self):
        fish_position_x = np.random.rand() * world_parameters.SCREEN_WIDTH
        fish_position_y = np.random.rand() * world_parameters.SCREEN_HEIGHT
        self.fishes.append(fish.Fish(len(self.fishes), fish_position_x, fish_position_y))

