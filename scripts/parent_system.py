import numpy as np
from scripts import world_parameters


class ParentSystem():
    def __init__():
        pass

    # Compute the average position of all neighbors of a fish
    # Returns position of fish if the fish has no neighbors
    def calculate_center_of_mass_neighbors(self, fish):
        if len(fish.neighbors) == 0:
            return fish.position_x, fish.position_y

        center_of_mass_x = 0
        center_of_mass_y = 0
        for neighbor in fish.neighbors:
            center_of_mass_x += neighbor.position_x
            center_of_mass_y += neighbor.position_y
        center_of_mass_x /= len(fish.neighbors)
        center_of_mass_y /= len(fish.neighbors)

        return center_of_mass_x, center_of_mass_y

    # Cohesion rule: steer the fish toward the center of mass of its neighbors
    # Divides by 100 to produce a gentle pull
    def cohesion_rule(self, fish):
        center_of_mass_x, center_of_mass_y = self.calculate_center_of_mass_neighbors(fish)
        speed_cohesion_rule_x = (center_of_mass_x - fish.position_x) / 100
        speed_cohesion_rule_y = (center_of_mass_y - fish.position_y) / 100
        return speed_cohesion_rule_x, speed_cohesion_rule_y