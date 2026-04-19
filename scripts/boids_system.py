import numpy as np
from scripts import world_parameters, parent_system

# Implements the three classic Boids rules (cohesion, separation, alignment)
# that produce emergent flocking behaviour
class BoidSystem(parent_system.ParentSystem):
    def __init__(self):
        pass

    # Separation rule: push the fish away from neighbors that are too close
    # Only neighbors within SEPARATION_RANGE contribute a repulsion force
    def separation_rule(self, fish):
        speed_separation_rule_x, speed_separation_rule_y = 0, 0
        for neighbor in fish.neighbors:
            if fish.distance_to(neighbor.position_x, neighbor.position_y) < world_parameters.SEPARATION_RANGE:
                speed_separation_rule_x += fish.position_x - neighbor.position_x
                speed_separation_rule_y += fish.position_y - neighbor.position_y
        return speed_separation_rule_x, speed_separation_rule_y

    # Compute the average velocity of all neighbors of a fish
    # Returns (0, 0) if the fish has no neighbors
    def calculate_mean_speed_neighbors(self, fish):
        if len(fish.neighbors) == 0:
            return 0, 0

        mean_speed_of_neighbors_x, mean_speed_of_neighbors_y = 0, 0
        for neighbor in fish.neighbors:
            mean_speed_of_neighbors_x += neighbor.speed_x
            mean_speed_of_neighbors_y += neighbor.speed_y
        mean_speed_of_neighbors_x /= len(fish.neighbors)
        mean_speed_of_neighbors_y /= len(fish.neighbors)

        return mean_speed_of_neighbors_x, mean_speed_of_neighbors_y

    # Alignment rule: steer the fish to match the average velocity of its neighbors
    # Divides by 5 to produce a moderate alignment pull
    def alignment_rule(self, fish):
        mean_speed_of_neighbors_x, mean_speed_of_neighbors_y = self.calculate_mean_speed_neighbors(fish)
        speed_alignment_rule_x = (mean_speed_of_neighbors_x - fish.speed_x) / 5
        speed_alignment_rule_y = (mean_speed_of_neighbors_y - fish.speed_y) / 5
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
