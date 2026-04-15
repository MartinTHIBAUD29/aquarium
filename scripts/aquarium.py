import numpy as np
from scripts import world_parameters, fish, boids_system, food

class Aquarium():
    def __init__(self):
        self.fishes = []
        self.foods = []
        self.create_n_fishes(world_parameters.INITIAL_NUMBER_OF_FISH)
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

    def add_new_food(self, food_position_x = None, food_position_y= None):
        if food_position_x == None:
            food_position_x = np.random.rand() * world_parameters.SCREEN_WIDTH
        if food_position_y == None:    
            food_position_y = np.random.rand() * world_parameters.SCREEN_HEIGHT

        self.foods.append(food.Food(food_position_x, food_position_y))

    def find_fish_neighbors(self, fish):
        fish.neighbors = []
        for other in self.fishes:
            if fish.distance_to(other.position_x, other.position_y) < fish.field_of_view:
                fish.neighbors.append(other)

    def find_food_in_sight(self, fish):
        fish.food_in_sight = {}
        food_to_remove = []
        for food in self.foods:
            distance_to_food = fish.distance_to(food.position_x, food.position_y)
            if distance_to_food < world_parameters.FOOD_SIZE:
                food_to_remove.append(food)
            elif distance_to_food < food.range_of_detection:
                    fish.food_in_sight[food] = distance_to_food
        for food in food_to_remove:
            self.foods.remove(food)
        

    def update_fishes_neighborhood(self):        
        for current_fish in self.fishes:
            self.find_fish_neighbors(current_fish)
            
            self.find_food_in_sight(current_fish)


    def update_fishes_position(self):
        self.update_fishes_neighborhood()
        for fish in self.fishes:
            fish.update_position(self.boids_calculation)

                
        

    
    

