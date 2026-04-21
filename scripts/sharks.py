
import numpy as np
from scripts import creature, world_parameters

class Shark(creature.Creature):
    def __init__(self, position_x, position_y):
        self.field_of_view = world_parameters.SHARK_FIELD_OF_VIEW
        self.color = world_parameters.SHARK_COLOR
        self.max_speed = world_parameters.SHARK_MAX_SPEED
        super().__init__(position_x, position_y)

 

    def calculate_speed(self, boids_calculation, sharks_calculation):
        self.max_speed = world_parameters.SHARK_MAX_SPEED
        last_speed_x = self.speed_x
        last_speed_y = self.speed_y

        if self.neighbors != []:
            speed_cohesion_rule_x, speed_cohesion_rule_y = sharks_calculation.chase_closest_fish(self)
            self.speed_x += speed_cohesion_rule_x
            self.speed_y += speed_cohesion_rule_y
            self.max_speed = world_parameters.SHARK_MAX_SPEED_IN_CHASE

        elif np.random.rand() < world_parameters.RANDON_MOVEMENT_PROBABILITY:
            _angle = 2 * np.pi * np.random.rand()
            _speed = self.max_speed * (0.7 + 0.3 * np.random.rand())
            self.speed_x, self.speed_y = _speed * np.cos(_angle), _speed * np.sin(_angle)  # Initial speed is random

        self.handle_obstacles()
        self.limit_speed()




