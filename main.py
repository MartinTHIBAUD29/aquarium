import pygame
from scripts import aquarium, ui


def run():
    pygame.init()

    interface = ui.UserInterface() 
    tank = aquarium.Aquarium()

    while interface.running:
        for event in pygame.event.get():
            interface.handle_event(event, tank)

        tank.simulate_step()

        interface.render_tank(tank)

    pygame.quit()

    
if __name__ == "__main__": 
    run()
