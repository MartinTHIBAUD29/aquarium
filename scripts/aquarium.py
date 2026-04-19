import numpy as np
from scripts import world_parameters, fish, boids, boids_system, food, spatial_grid

class Aquarium():
    def __init__(self):
        self.fishes = [] #List of all fish objects in the simulation
        self.foods = [] #List of all food objects in the simulation
        self.create_n_fishes(world_parameters.INITIAL_NUMBER_OF_FISH)
        self.boids_calculation = boids_system.BoidsSystem() #used for calculation of the 3 boids rules
        self.grid_calculation = spatial_grid.SpatialGrid() #used for separating the screen in smaller cases
                                                           #used for reducing the number of calculation each step


    def create_n_fishes(self, number_of_fish):
        for i in range(number_of_fish):
            self.add_new_entity("fish")

    # Create either a food or a fish object
    # if no position is specified, the object is created at a random location
    def add_new_entity(self, type_of_entity, position_x = None, position_y= None):
        tank_margin = world_parameters.TANK_MARGIN
        if position_x == None:
            position_x = np.random.rand() * (world_parameters.SCREEN_WIDTH -  2 *tank_margin ) + tank_margin
        if position_y == None:    
            position_y = np.random.rand() * (world_parameters.SCREEN_HEIGHT- 2 *tank_margin ) + tank_margin
        if type_of_entity == "fish":
            self.fishes.append(boids.Boids(position_x, position_y))
        elif type_of_entity == "food":
            self.foods.append(food.Food(position_x, position_y))

    #Each step if a food has been eaten, remove it from the aquarium
    def remove_foods_from_list(self, food_to_remove):
        for food in food_to_remove:
            self.foods.remove(food)

    # Each step, update for all fishes in the simulation:
    # - the list of its neighbors
    # - list of food in sight
    # Remove foods that are in range of being eaten
    def refresh_neighborhood(self):
        self.grid_calculation.update_grid(self.fishes, self.foods)        
        for current_fish in self.fishes:
            self.grid_calculation.find_fish_neighbors(current_fish, self.fishes)
            
            food_to_remove = self.grid_calculation.find_food_in_sight(current_fish, self.foods)
            self.remove_foods_from_list(food_to_remove)

    # Function called by main to update the Aquarium each step
    # 1st update the list of neighbors / food of all fishes
    # 2nd calculate next cycle fish position
    def simulate_step(self):
        self.refresh_neighborhood()
        for fish in self.fishes:
            fish.move(self.boids_calculation)

                
        

    
    

