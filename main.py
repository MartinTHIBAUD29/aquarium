import sys
import pygame
from scripts import ui, simulation



def run():
    pygame.init()

    
    screen = ui.start_ui()
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        simulation.update_position()
        ui.render(screen, player_pos)

    pygame.quit()

    
if __name__ == "__main__": 
    run()
