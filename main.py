import sys
import pygame
from scripts import simulation, ui


def run():
    pygame.init()

    user_interface = ui.UserInterface()
    aquarium = simulation.Aquarium()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        aquarium.update_position()

        user_interface.render(aquarium.fish_position)

    pygame.quit()

    
if __name__ == "__main__": 
    run()
