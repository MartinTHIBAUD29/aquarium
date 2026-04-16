import numpy as np
from scripts import world_parameters, fish, boids_system, food, spatial_grid

class Aquarium():
    def __init__(self):
        self.fishes = []
        self.foods = []
        self.create_n_fishes(world_parameters.INITIAL_NUMBER_OF_FISH)
        self.boids_calculation = boids_system.BoidsSystem()
        self.grid_calculation = spatial_grid.SpatialGrid()

    def create_n_fishes(self, number_of_fish):
        for i in range(number_of_fish):
            self.add_new_entity("fish")

    def add_new_entity(self, type_of_entity, position_x = None, position_y= None):
        if position_x == None:
            position_x = np.random.rand() * world_parameters.SCREEN_WIDTH
        if position_y == None:    
            position_y = np.random.rand() * world_parameters.SCREEN_HEIGHT
        if type_of_entity == "fish":
            self.fishes.append(fish.Fish(position_x, position_y))
        elif type_of_entity == "food":
            self.foods.append(food.Food(position_x, position_y))


    def remove_food_from_list(self, food_to_remove):
        for food in food_to_remove:
            self.foods.remove(food)

    def update_fishes_neighborhood(self):        
        for current_fish in self.fishes:
            self.grid_calculation.find_fish_neighbors(current_fish, self.fishes)
            
            food_to_remove = self.grid_calculation.find_food_in_sight(current_fish, self.foods)
            self.remove_food_from_list(food_to_remove)



    def update_fishes_position(self):
        self.update_fishes_neighborhood()
        for fish in self.fishes:
            fish.update_position(self.boids_calculation)

                
        

    
    

