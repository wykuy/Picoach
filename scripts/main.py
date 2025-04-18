import pygame
import sys
from ui import UI
from interval_setup import setup_intervals
from workout import start_workout
from config import load_config, save_config
from history import log_workout

def main():
    # Initialize pygame
    pygame.init()

    # Set screen dimensions based on the display
    screen = pygame.display.set_mode((320, 480))  # Assuming a 320x480 resolution for now
    
    # Set up the initial UI
    ui = UI(screen)

    # Load configuration (brightness, boat type, etc.)
    config = load_config()

    # Display the main menu
    ui.display_main_menu()

    # Main event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the program on close
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Handle button presses based on their positions
                if ui.is_main_menu_button_pressed(x, y):
                    ui.display_interval_setup()
                elif ui.is_interval_setup_button_pressed(x, y):
                    # Setup intervals
                    work_time, rest_time, intervals = setup_intervals()
                    save_config({'work_time': work_time, 'rest_time': rest_time, 'intervals': intervals})
                    ui.display_workout_screen()
                elif ui.is_workout_start_button_pressed(x, y):
                    # Start the workout with selected intervals
                    work_time, rest_time, intervals = load_config()
                    start_workout(work_time, rest_time, intervals)
                    ui.display_workout_complete()
                elif ui.is_history_button_pressed(x, y):
                    ui.display_history_viewer()

        pygame.display.update()  # Refresh screen after processing input

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
