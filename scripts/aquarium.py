import numpy as np
from scripts import world_parameters, fish, boids_system

class Aquarium():
    def __init__(self):
        self.fishes = []
        self.create_n_fishes(world_parameters.NUMBER_OF_FISH)
        self.boids_calculation = boids_system.BoidsSystem()

    def create_n_fishes(self, number_of_fish):
        for i in range(number_of_fish):
            self.add_new_fish()

    def add_new_fish(self, fish_position_x = None, fish_position_y= None):
        if fish_position_x == None:
            fish_position_x = np.random.rand() * world_parameters.SCREEN_WIDTH
        if fish_position_y == None:    
            fish_position_y = np.random.rand() * world_parameters.SCREEN_HEIGHT

        self.fishes.append(fish.Fish(fish_position_x, fish_position_y))

    def update_fishes_neighborhood(self):        
        for current_fish in self.fishes: 
            current_fish.neighbors = []
            for other in self.fishes:
                if current_fish.distance_to(other) < current_fish.field_of_view:
                    current_fish.neighbors.append(other)
     
    def update_fishes_position(self):
        self.update_fishes_neighborhood()
        for fish in self.fishes:
            fish.update_position(self.boids_calculation)
            
    
    

