import pygame
import numpy as np
from scripts import world_parameters

class UserInterface:
    def __init__(self):
        self.running = True
        self.size = (world_parameters.SCREEN_WIDTH, world_parameters.SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)

    
    # Method used to compute three points around a fish position
    # 1st point is in the direction of the fish, at a distane 1.5 * fish_size
    # Points 2 and 3 are in the back of the fish, symetric and at a distance 1* fish_size
    # return a list with of 3 tuples, each tuple is the coordinates of the points
    def calculate_triangle_points(self, fish): 
        fish_direction = np.degrees(np.arctan2(fish.speed_y, fish.speed_x))
        fish_direction = (fish_direction + 180) % 360 - 180
        fish_size = world_parameters.FISH_SIZE

        point1_x = fish.position_x  + np.cos(np.deg2rad(fish_direction)) * 1.5 * fish_size
        point1_y = fish.position_y  + np.sin(np.deg2rad(fish_direction)) * 1.5 * fish_size

        point2_x = fish.position_x  + np.cos(np.deg2rad(fish_direction + 130)) * fish_size
        point2_y = fish.position_y  + np.sin(np.deg2rad(fish_direction + 130)) * fish_size

        point3_x = fish.position_x  + np.cos(np.deg2rad(fish_direction - 130)) * fish_size
        point3_y = fish.position_y  + np.sin(np.deg2rad(fish_direction - 130)) * fish_size

        return([(point1_x, point1_y), (point2_x, point2_y), (point3_x, point3_y)])

    # Draw a fish as a filled triangle pointing in its direction of movement
    # Calls calculate_triangle_points to get the triangle corners
    def render_fish(self, fish):
        pygame.draw.polygon(self.screen, fish.color, 
                           self.calculate_triangle_points(fish) , width=0)


    # Draw a food as a square of side world_parameters.FOOD_SIZE centered around its position
    def render_food(self, food):
         food_size = world_parameters.FOOD_SIZE
         pygame.draw.rect(self.screen, world_parameters.FOOD_COLOR, 
                          (food.position_x - (food_size/2), food.position_y - (food_size/2), food_size, food_size))


    # Clear the screen and draw all fishes and foods contained in the aquarium
    def render_tank(self, aquarium):
        self.screen.fill((0, 0, 0)) 
        for fish in aquarium.fishes:
            self.render_fish(fish)
        for food in aquarium.foods:
            self.render_food(food)
        
        pygame.display.flip()

    # Catch pygame Events:
    # - Close window stops the simulation
    # - SpaceBar adds a new fish at a random position
    # - Mouse click adds a food at the click position
    def handle_event(self, event, aquarium):
        if event.type == pygame.QUIT:
                self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aquarium.add_new_entity("shark")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            aquarium.add_new_entity("food", *event.pos)
        



