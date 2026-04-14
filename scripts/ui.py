import pygame
from scripts import world_parameters

class UserInterface:
    def __init__(self):
        self.running = True
        self.size = (world_parameters.SCREEN_WIDTH, world_parameters.SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)

    def render(self, aquarium):
        self.screen.fill((0, 0, 0))  # clear screen (black)
        for fish in aquarium.fishes:
            pygame.draw.circle(self.screen, (255, 0, 0), (fish.position_x, fish.position_y), 5)

        for food in aquarium.foods:
            pygame.draw.rect(self.screen, (0, 255, 0), (food.position_x - 5, food.position_y - 5, 10, 10))

        pygame.display.flip()

    def handle_event(self, event, aquarium):
        if event.type == pygame.QUIT:
                self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aquarium.add_new_fish()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            aquarium.add_new_food(*event.pos)
        



