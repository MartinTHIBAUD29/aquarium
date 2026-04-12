import pygame
from scripts import world_parameters

class UserInterface:
    def __init__(self):
        self.running = True
        self.size = (world_parameters.SCREEN_WIDHT, world_parameters.SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)

    def render(self, fish):
        pygame.draw.circle(self.screen, (255, 0, 0), fish.position, 20)
        pygame.display.flip()




