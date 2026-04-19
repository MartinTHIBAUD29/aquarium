import numpy as np
from scripts import fish, world_parameters

class Boid(fish.Fish):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.food_in_sight = {} #Dict of {food: distance} for food within detection range, updated each step
        self.field_of_view = world_parameters.FISH_FIELD_OF_VIEW
        self.color = world_parameters.FISH_COLOR

    # Apply the boids speed contribution calculated by BoidsSystem to this fish velocity
    def calculate_boids_speed(self, boids_calculation):
        boids_speed_x, boids_speed_y = boids_calculation.calculate_boids_speed(self)
        self.speed_x += boids_speed_x
        self.speed_y += boids_speed_y

    # Steer the fish toward the closest food in its food_in_sight dict
    def go_for_closest_food(self):
        closest_food = min(self.food_in_sight, key = self.food_in_sight.get)

        speed_x = (closest_food.position_x - self.position_x) / 100
        speed_y = (closest_food.position_y - self.position_y) / 100

        self.speed_x += speed_x
        self.speed_y += speed_y


    # Determine the fish velocity for this step:
    # - Small random chance: apply a random direction change (wandering)
    # - No food in sight: apply the three boids rules and wall avoidance
    # - Food in sight: steer toward the closest food
    # After all contributions, clamp the speed to MAX_SPEED
    def calculate_speed(self, boids_calculation):
        last_speed_x = self.speed_x
        last_speed_y = self.speed_y

        if self.sharks_in_sight != []:
            boids_speed_x, boids_speed_y = boids_calculation.separation_rule(self)

        elif self.food_in_sight != {}:
            self.go_for_closest_food()

        elif np.random.rand() < world_parameters.RANDOWN_MOVEMENT_PROBABILITY:
            self.speed_x, self.speed_y = np.random.rand() - 0.5 , np.random.rand() - 0.5
            self.smooth_rotation(last_speed_x, last_speed_y, 45)

        else:
            self.calculate_boids_speed(boids_calculation)
            self.handle_obstacles()
            self.smooth_rotation(last_speed_x, last_speed_y)

        self.limit_speed(world_parameters.MAX_SPEED)

