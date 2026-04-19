
import numpy as np
from scripts import creature, world_parameters

class Shark(creature.Creature):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.field_of_view = world_parameters.SHARK_FIELD_OF_VIEW
        self.color = world_parameters.SHARK_COLOR


    def calculate_speed(self, boids_calculation, sharks_calculation):
        last_speed_x = self.speed_x
        last_speed_y = self.speed_y

        if self.neighbors != {}:
            speed_cohesion_rule_x, speed_cohesion_rule_y = sharks_calculation.cohesion_toward_fish(self)
            self.speed_x += speed_cohesion_rule_x
            self.speed_y += speed_cohesion_rule_y


        elif np.random.rand() < world_parameters.RANDOWN_MOVEMENT_PROBABILITY:
            self.speed_x, self.speed_y = np.random.rand() - 0.5 , np.random.rand() - 0.5
            self.smooth_rotation(last_speed_x, last_speed_y, 45)

        self.handle_obstacles()
        self.limit_speed(world_parameters.MAX_SPEED)




