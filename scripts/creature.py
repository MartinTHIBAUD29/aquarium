import numpy as np
from scripts import world_parameters

class Creature:
    def __init__(self, position_x, position_y):
        self.position_x,  self.position_y = position_x, position_y
        self.speed_x, self.speed_y = 2* np.random.rand() - 1 , 2* np.random.rand() - 1 #Initial speed is random
        self.neighbors = [] #List of fish within field of view, updated each step
        self.sharks_in_sight = []
        
        
    # Return the euclidean distance between this fish and any (x, y) position
    def distance_to(self, object_position_x, object_position_y):
        distance = np.sqrt(
                (self.position_x - object_position_x)**2 + 
                ((self.position_y - object_position_y)**2))
        return distance


    # Push the fish away from tank walls when it enters the margin zone
    # Push strength increases proportionally to how deep into the margin the fish is
    def handle_obstacles(self):
        margin = world_parameters.TANK_MARGIN
        push_strength = world_parameters.WALL_PUSH_STRENGHT

        if self.position_x < margin:
            self.speed_x += push_strength * (margin - self.position_x)
        elif self.position_x > world_parameters.SCREEN_WIDTH - margin:
            self.speed_x -= push_strength * (self.position_x - (world_parameters.SCREEN_WIDTH - margin))

        if self.position_y < margin:
            self.speed_y += push_strength * (margin - self.position_y)
        elif self.position_y > world_parameters.SCREEN_HEIGHT - margin:
            self.speed_y -= push_strength * (self.position_y - (world_parameters.SCREEN_HEIGHT - margin))


    # Limit the turn applied this step to max_turn_deg degrees
    # Keeps the total speed magnitude unchanged, only rotates the direction
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

    def limit_speed(self, max_speed):
        speed = np.sqrt(self.speed_x**2 + self.speed_y**2)
        if speed > max_speed:
            self.speed_x = (self.speed_x / speed) * max_speed
            self.speed_y = (self.speed_y / speed) * max_speed
            
    # Update the fish velocity then advance its position by one step
    # Clamp position to screen bounds to prevent escaping the tank
    def move(self, boids_calculation, sharks_calculation):
        self.calculate_speed(boids_calculation, sharks_calculation)
        self.position_x += self.speed_x
        self.position_y += self.speed_y
        self.position_x = max(0, min(self.position_x, world_parameters.SCREEN_WIDTH))
        self.position_y = max(0, min(self.position_y, world_parameters.SCREEN_HEIGHT))
