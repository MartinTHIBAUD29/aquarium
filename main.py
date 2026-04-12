import sys
import pygame
from scripts import aquarium, ui


def run():
    pygame.init()

    interface = ui.UserInterface()
    tank = aquarium.Aquarium()

    while interface.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                interface.running = False

        tank.update_fishes_position()

        interface.render(tank.fishes)

    pygame.quit()

    
if __name__ == "__main__": 
    run()
