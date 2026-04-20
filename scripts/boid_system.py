import numpy as np
from scripts import world_parameters, parent_system

# Implements the three classic Boids rules (cohesion, separation, alignment)
# that produce emergent flocking behaviour
class BoidSystem(parent_system.ParentSystem):
    def __init__(self):
        pass


    # Cohesion rule: steer the fish toward the center of mass of its neighbors
    # Divides by 100 to produce a gentle pull
    # if the list of neighbors is empty, cohesion speed is set to 0
    def cohesion_rule(self, fish):
        center_of_mass_x, center_of_mass_y = self.calculate_center_of_mass_neighbors(fish.neighbors)
        if (center_of_mass_x != None and center_of_mass_y != None) :
            speed_cohesion_rule_x = (center_of_mass_x - fish.position_x) / 100
            speed_cohesion_rule_y = (center_of_mass_y - fish.position_y) / 100
        else: 
            speed_cohesion_rule_x = 0
            speed_cohesion_rule_y = 0
        return speed_cohesion_rule_x, speed_cohesion_rule_y
    
    # Separation rule: push the fish away from neighbors that are too close
    # Only neighbors within SEPARATION_RANGE contribute a repulsion force
    def separation_rule(self, fish):
        speed_separation_rule_x, speed_separation_rule_y = 0, 0
        fish_in_separation_range = []
        for neighbor in fish.neighbors:
            if fish.distance_to(neighbor) < world_parameters.SEPARATION_RANGE:
                fish_in_separation_range.append(neighbor)

        center_of_mass_x, center_of_mass_y = self.calculate_center_of_mass_neighbors(fish_in_separation_range)
        if (center_of_mass_x != None and center_of_mass_y != None) : 
            speed_separation_rule_x = fish.position_x - center_of_mass_x
            speed_separation_rule_y = fish.position_y - center_of_mass_y
        else:
            speed_separation_rule_x = 0
            speed_separation_rule_y = 0
        return speed_separation_rule_x, speed_separation_rule_y


    # Alignment rule: steer the fish to match the average velocity of its neighbors
    # Divides by 5 to produce a moderate alignment pull
    # if the list of neighbors is empty, aligment speed is set to 0
    def alignment_rule(self, fish):
        mean_speed_of_neighbors_x, mean_speed_of_neighbors_y = self.calculate_mean_speed_neighbors(fish.neighbors)
        if (mean_speed_of_neighbors_x != None and mean_speed_of_neighbors_y != None) :
            speed_alignment_rule_x = (mean_speed_of_neighbors_x - fish.speed_x) / 5
            speed_alignment_rule_y = (mean_speed_of_neighbors_y - fish.speed_y) / 5
        else:
            speed_alignment_rule_x = 0
            speed_alignment_rule_y = 0
        return speed_alignment_rule_x, speed_alignment_rule_y

    # Combine all three boids rules, weighted by their respective ratios
    # Returns the total (x, y) speed contribution to apply to the fish this step
    def calculate_boids_speed(self, fish):
        speed_cohesion_rule_x, speed_cohesion_rule_y = self.cohesion_rule(fish)
        speed_separation_rule_x, speed_separation_rule_y = self.separation_rule(fish)
        speed_alignment_rule_x, speed_alignment_rule_y = self.alignment_rule(fish)

        boids_speed_x = (world_parameters.COHESION_RATIO * speed_cohesion_rule_x
                         + world_parameters.SEPARATION_RATIO * speed_separation_rule_x
                         + world_parameters.ALIGNMENT_RATIO * speed_alignment_rule_x)

        boids_speed_y = (world_parameters.COHESION_RATIO * speed_cohesion_rule_y
                         + world_parameters.SEPARATION_RATIO * speed_separation_rule_y
                         + world_parameters.ALIGNMENT_RATIO * speed_alignment_rule_y)

        return (boids_speed_x, boids_speed_y)
