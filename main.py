import pygame
from scripts import aquarium, ui


# Entry point for the aquarium simulation
# Initialises pygame, creates the tank and interface, then runs the main loop:
# 1. Process input events (quit, add fish, add food)
# 2. Advance the simulation by one step
# 3. Render the updated state to the screen
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
