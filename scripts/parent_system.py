import numpy as np
from scripts import world_parameters


class ParentSystem():
    def __init__():
        pass

    # Compute the average position of all fishes in a list
    # Returns None if the list is empty
    def calculate_center_of_mass_neighbors(self, list_of_fish):
        if len(list_of_fish) == 0:
            return None, None

        center_of_mass_x = 0
        center_of_mass_y = 0
        for fish in list_of_fish:
            center_of_mass_x += fish.position_x
            center_of_mass_y += fish.position_y
        center_of_mass_x /= len(list_of_fish)
        center_of_mass_y /= len(list_of_fish)

        return center_of_mass_x, center_of_mass_y

    # Compute the average velocity of all fishes in a list
    # Returns None if the list is empty
    def calculate_mean_speed_neighbors(self, list_of_fish):
        if len(list_of_fish) == 0:
            return None, None

        mean_speed_of_neighbors_x, mean_speed_of_neighbors_y = 0, 0
        for fish in list_of_fish:
            mean_speed_of_neighbors_x += fish.speed_x
            mean_speed_of_neighbors_y += fish.speed_y
        mean_speed_of_neighbors_x /= len(list_of_fish)
        mean_speed_of_neighbors_y /= len(list_of_fish)

        return mean_speed_of_neighbors_x, mean_speed_of_neighbors_y