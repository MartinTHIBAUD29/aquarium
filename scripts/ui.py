import pygame
from scripts import world_parameters


class UserInterface:
    def __init__(self):
        self.size = (world_parameters.SCREEN_WIDHT, world_parameters.SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)

    def render(self, player_pos):
        pygame.draw.circle(self.screen, (255, 0, 0), player_pos, 20)
        pygame.display.flip()




