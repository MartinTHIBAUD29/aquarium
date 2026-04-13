import numpy as np
from scripts import world_parameters

class Fish:
    def __init__(self, identification, position_x, position_y):
        self.identification = identification
        self.position_x,  self.position_y = position_x, position_y
        self.speed_x, self.speed_y = np.random.rand() - 0.5 , np.random.rand() - 0.5 
        self.neighbors = []
        #self.field_of_view = (np.random.rand() + 0.5) * 40
        self.field_of_view = 40
        

    def distance_to(self, fish):
        distance = np.sqrt(
                (self.position_x - fish.position_x)**2 + 
                ((self.position_y - fish.position_y)**2))
        return distance
    

    def calculate_center_of_mass_neighbors(self):

        if len(self.neighbors) == 0:
            return 
        
        center_of_mass_x = 0
        center_of_mass_y = 0
        for neighbor in self.neighbors:
            center_of_mass_x += neighbor.position_x
            center_of_mass_y += neighbor.position_y
        center_of_mass_x /= len(self.neighbors)
        center_of_mass_y /= len(self.neighbors)

        return center_of_mass_x, center_of_mass_y


    def concentration_rule(self):
        center_of_mass_x, center_of_mass_y = self.calculate_center_of_mass_neighbors()
        speed_contration_rule_x = (self.position_x - center_of_mass_x) / 100
        speed_contration_rule_y = (self.position_y - center_of_mass_y) / 100
        return speed_contration_rule_x , speed_contration_rule_y


    def calculate_speed(self):
        speed_contration_rule_x, speed_contration_rule_y = self.concentration_rule()
        self.speed_x -= speed_contration_rule_x
        self.speed_y -= speed_contration_rule_y

        max_speed = 1
        speed = np.sqrt(self.speed_x**2 + self.speed_y**2)

        if speed > max_speed:
            self.speed_x = (self.speed_x / speed) * max_speed
            self.speed_y = (self.speed_y / speed) * max_speed


    def update_position(self):
        self.calculate_speed()
        self.position_x += self.speed_x
        self.position_y += self.speed_y
