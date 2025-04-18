import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 24)
        self.screen.fill((0, 0, 0))  # Fill the screen with black

    def display_main_menu(self):
        # This function would display the main menu of the PiCoach
        self.screen.fill((255, 255, 255))  # White background for the menu
        self.display_text("PiCoach", 100, 100, (0, 0, 0))  # Title text
        pygame.display.flip()

    def display_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
