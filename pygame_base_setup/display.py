import pygame
from colors import *


class Display:
    def __init__(self, simulation, resolution):

        # Initialize fonts
        self.debug_font = pygame.font.SysFont('Arial', 14)

        self.sim = simulation
        self.res = resolution

        """SURFACES"""

        self.debug_info_surface = pygame.Surface(size=(100, 60), flags=pygame.SRCALPHA)  # Flag enables transparency

        """DISPLAY STATES"""

        self.show_debug_info = True

        """GAME VARIABLES"""

        self.delta_time_last_frame = 1

    def process_events(self):
        """
        Process input events by the user
        :return State of simulation. True = Simulation ended.
        """
        for event in pygame.event.get():

            # CASE: Game closed
            if event.type == pygame.QUIT:
                return True

            elif event.type == pygame.KEYDOWN:
                """KEY PRESS CASES"""
                pass

        return False

    def update(self, delta_time_last_frame):
        """
        Update display values.
        :param delta_time_last_frame: time since last frame draw. used to display fps in debug infos
        """
        # Update frame time
        self.delta_time_last_frame = delta_time_last_frame

    def render(self, screen):
        """
        Draw the current state of the simulation to a screen
        :param screen: pygame screen to draw the game objects on
        """

        # Reset screen
        screen.fill(black)

        """SIMULATION DISPLAY"""

        # Get current simulation state
        sim_state = self.sim.get_state()

        """DEBUG DISPLAY"""

        # Display simulation infos
        if self.show_debug_info:
            self.draw_debug_info(screen, location=(0, 0))

    def draw_debug_info(self, screen, location):
        """
        Draw the debug info to the debug info surface and place onto the defined screen
        :param screen: Screen on which the debug info surface gets blit
        :param location: location on the screen for the blit
        """

        # Reset debug info surface
        self.debug_info_surface.fill((0, 0, 0, 0))  # Fill with transparent background

        # Draw FPS to surface
        text_surface = self.debug_font.render(f"FPS: {round(1 / self.delta_time_last_frame)}", True, white)
        self.debug_info_surface.blit(text_surface, (2, 0))

        # Draw debug info surface to main screen
        screen.blit(self.debug_info_surface, location)
