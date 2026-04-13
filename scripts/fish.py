import numpy as np
from scripts import world_parameters

class Fish:
    def __init__(self, identification, position_x, position_y):
        self.identification = identification
        self.position_x,  self.position_y = position_x, position_y
        self.speed_x, self.speed_y = np.random.rand() - 0.5, np.random.rand() - 0.5
        self.neighbors = []
        self.field_of_view = np.random.rand() + 0.5 * 30  # distance within which the fish can see other fishes

    def distance_to(self, fish):
        distance = np.sqrt(
                (self.position_x - fish.position_x)**2 + 
                ((self.position_y - fish.position_y)**2))
        return distance
    
    def calculate_speed(self):
        pass

    def update_position(self):
        self.position_x += self.speed_x
        self.position_y += self.speed_y
