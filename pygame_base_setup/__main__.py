import pygame
from typing import Tuple
from simulation import Simulation
from display import Display


def run_game(target_fps: int = 60, resolution: Tuple[int, int] = (720, 480)):
    """
    Run the main loop of the simulation/display
    :param target_fps: The max FPS value
    :param resolution: Resolution of the display window
    """

    # Initialize pygame and set up the window
    pygame.init()
    pygame.display.set_caption("Simulation")
    screen = pygame.display.set_mode(resolution)

    # Create simulation loop variables
    done = False
    clock = pygame.time.Clock()
    delta_time_last_frame = 1

    # Create simulation and display instances
    simulation = Simulation()
    display = Display(simulation=simulation, resolution=resolution)

    """ MAIN GAME LOOP """

    while not done:
        # Run all simulation functions for one step/frame of the simulation
        done = display.process_events()
        simulation.update()
        display.update(delta_time_last_frame)
        display.render(screen)

        # Display updated screen
        pygame.display.flip()

        # Tick game and save time this frame took to compute
        delta_time_last_frame = clock.tick(target_fps) / 1000


if __name__ == '__main__':
    run_game(target_fps=60)
