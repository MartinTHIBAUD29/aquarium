import pygame
from scripts import world_parameters

def start_ui():
    size = (world_parameters.SCREEN_WIDHT, world_parameters.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    return screen






