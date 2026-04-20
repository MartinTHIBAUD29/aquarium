import numpy as np
from scripts import world_parameters, parent_system

class SharkSystem(parent_system.ParentSystem):
    def __init__(self):
        pass


    # Steers the shark directly toward the closest visible fish.
    # Returns (0, 0) if no neighbors are visible.
    def chase_closest_fish(self, shark):
        closest = self.find_closest_fish(shark, shark.neighbors)
        if closest is None:
            return 0, 0
        speed_x = (closest.position_x - shark.position_x) / 100
        speed_y = (closest.position_y - shark.position_y) / 100
        return speed_x, speed_y

    # Steers the shark toward the center of mass of all visible fish.
    # Returns (0, 0) if no neighbors are visible.
    def cohesion_toward_fish(self, shark):
        center_of_mass_x, center_of_mass_y = self.calculate_center_of_mass_neighbors(shark.neighbors)
        if (center_of_mass_x is not None and center_of_mass_y is not None) :
            speed_cohesion_rule_x = (center_of_mass_x - shark.position_x) / 100
            speed_cohesion_rule_y = (center_of_mass_y - shark.position_y) / 100
        else: 
            speed_cohesion_rule_x = 0
            speed_cohesion_rule_y = 0
        return speed_cohesion_rule_x, speed_cohesion_rule_y


    def separation_from_sharks(self, fish):
        speed_separation_rule_x, speed_separation_rule_y = 0, 0
        center_of_mass_x, center_of_mass_y = self.calculate_center_of_mass_neighbors(fish.sharks_in_sight)
        if (center_of_mass_x != None and center_of_mass_y != None) : 
            speed_separation_rule_x = fish.position_x - center_of_mass_x
            speed_separation_rule_y = fish.position_y - center_of_mass_y
        else:
            speed_separation_rule_x = 0
            speed_separation_rule_y = 0
        return speed_separation_rule_x, speed_separation_rule_y