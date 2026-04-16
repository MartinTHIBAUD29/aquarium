import numpy as np
from scripts import world_parameters

class Fish:
    def __init__(self, position_x, position_y):
        self.position_x,  self.position_y = position_x, position_y
        self.speed_x, self.speed_y = np.random.rand() - 0.5 , np.random.rand() - 0.5 
        self.neighbors = []
        self.food_in_sight = {}
        self.field_of_view = world_parameters.FISH_FIELD_OF_VIEW
        

    def distance_to(self, object_position_x, object_position_y):
        distance = np.sqrt(
                (self.position_x - object_position_x)**2 + 
                ((self.position_y - object_position_y)**2))
        return distance
     

    def calculate_boids_speed(self, boids_calculation):
        
        boids_speed_x, boids_speed_y = boids_calculation.calculate_boids_speed(self)
        self.speed_x += boids_speed_x
        self.speed_y += boids_speed_y
    
    def handle_obstacles(self):
        margin = world_parameters.TANK_MARGIN      # start feeling the wall earlier
        push_strength = world_parameters.WALL_PUSH_STRENGHT

        # Distance-based inward push (stronger as fish gets closer)
        if self.position_x < margin:
            self.speed_x += push_strength * (margin - self.position_x)
        elif self.position_x > world_parameters.SCREEN_WIDTH - margin:
            self.speed_x -= push_strength * (self.position_x - (world_parameters.SCREEN_WIDTH - margin))

        if self.position_y < margin:
            self.speed_y += push_strength * (margin - self.position_y)
        elif self.position_y > world_parameters.SCREEN_HEIGHT - margin:
            self.speed_y -= push_strength * (self.position_y - (world_parameters.SCREEN_HEIGHT - margin))


    def smooth_rotation(self, last_speed_x, last_speed_y, max_turn_deg = world_parameters.MAX_TURN_DEG):
        speed = np.hypot(self.speed_x, self.speed_y)
    
        angle_last = np.degrees(np.arctan2(last_speed_y, last_speed_x))
        angle_current = np.degrees(np.arctan2(self.speed_y, self.speed_x))

        # Use the shortest angular distance in [-180, 180].
        rotation_angle = (angle_current - angle_last + 180) % 360 - 180
        clamped_rotation = np.clip(rotation_angle, -max_turn_deg, max_turn_deg)
        final_angle = angle_last + clamped_rotation

        self.speed_x = np.cos(np.deg2rad(final_angle)) * speed
        self.speed_y = np.sin(np.deg2rad(final_angle)) * speed

    def go_for_closest_food(self): 
        closest_food = min(self.food_in_sight, key = self.food_in_sight.get)

        speed_x = (closest_food.position_x - self.position_x) / 100
        speed_y = (closest_food.position_y - self.position_y) / 100
        
        self.speed_x += speed_x
        self.speed_y += speed_y


   
    def calculate_speed(self, boids_calculation):

        if np.random.rand() >  1 - world_parameters.RANDOWN_MOVEMENT_PROBABILITY:
            self.speed_x, self.speed_y = np.random.rand() - 0.5 , np.random.rand() - 0.5 

        elif self.food_in_sight == {}:
            last_speed_x = self.speed_x
            last_speed_y = self.speed_y
            self.calculate_boids_speed(boids_calculation)
            self.handle_obstacles()
            self.smooth_rotation(last_speed_x, last_speed_y)

        else:
            self.go_for_closest_food()

        max_speed = world_parameters.MAX_SPEED
        speed = np.sqrt(self.speed_x**2 + self.speed_y**2)
        if speed > max_speed:
            self.speed_x = (self.speed_x / speed) * max_speed
            self.speed_y = (self.speed_y / speed) * max_speed

    def move(self, boids_calculation):
        self.calculate_speed(boids_calculation)
        self.position_x += self.speed_x
        self.position_y += self.speed_y
