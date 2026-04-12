import sys
import pygame
from scripts import ui, simulation



def run():
    pygame.init()

    screen = ui.start_ui()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        simulation.update_position()
    pygame.quit()

    
if __name__ == "__main__": 
    run()
