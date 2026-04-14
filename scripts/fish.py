import numpy as np
from scripts import world_parameters

class Fish:
    def __init__(self, position_x, position_y):
        self.position_x,  self.position_y = position_x, position_y
        self.speed_x, self.speed_y = np.random.rand() - 0.5 , np.random.rand() - 0.5 
        self.neighbors = []
        self.food_in_sight = {}
        self.field_of_view = 60
        

    def distance_to(self, object_position_x, object_position_y):
        distance = np.sqrt(
                (self.position_x - object_position_x)**2 + 
                ((self.position_y - object_position_y)**2))
        return distance
     

    def calculate_boids_speed(self, boids_calculation):
        
        boids_speed_x, boids_speed_y = boids_calculation.calculate_boids_speed(self)
        self.speed_x += boids_speed_x
        self.speed_y += boids_speed_y
    
    def go_for_closest_food(self): 
        closest_food = min(self.food_in_sight, key = self.food_in_sight.get)

        speed_x = (closest_food.position_x - self.position_x) / 100
        speed_y = (closest_food.position_y - self.position_y) / 100
        
        self.speed_x += speed_x
        self.speed_y += speed_y


    def update_position(self, boids_calculation):
        if self.food_in_sight == {}:
            self.calculate_boids_speed(boids_calculation)
        else:
            self.go_for_closest_food()

        max_speed = 0.3
        speed = np.sqrt(self.speed_x**2 + self.speed_y**2)

        if speed > max_speed:
            self.speed_x = (self.speed_x / speed) * max_speed
            self.speed_y = (self.speed_y / speed) * max_speed

        self.position_x += self.speed_x
        self.position_y += self.speed_y
            
        self.handle_obstacles()

    def handle_obstacles(self):
        if self.position_x < 0 :
            self.speed_x = - self.speed_x
            self.position_x = 0

        elif self.position_x > world_parameters.SCREEN_WIDTH:
            self.speed_x = - self.speed_x
            self.position_x = world_parameters.SCREEN_WIDTH

        if self.position_y < 0 :
            self.speed_y = - self.speed_y
            self.position_y = 0

        elif self.position_y > world_parameters.SCREEN_HEIGHT :
            self.speed_y = - self.speed_y
            self.position_y = world_parameters.SCREEN_HEIGHT
        

