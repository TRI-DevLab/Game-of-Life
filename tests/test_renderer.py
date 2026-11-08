# This is a temp folder to test if the render file is doing its job.

import pygame
import sys 
import os

# Ensure that modules can be imported from the parent directory 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from simulation import create_grid
from renderer import Renderer
import config

def main():
     
    # Initialize pygame
    pygame.init()

    # create display window 
    screen = pygame.display.set_mode(
         (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    )

    pygame.display.set_caption("Game of Life - Renderer Test")


    # Create the simulation grid
    rows = config.WINDOW_HEIGHT // config.CELL_SIZE
    columns = config.WINDOW_WIDTH // config.CELL_SIZE

    grid = create_grid(rows, columns)


    # Add some living cells
    grid[4][3] = 1
    grid[4][4] = 1
    grid[4][5] = 1
    grid[5][4] = 1


    # Create the renderer 
    renderer = Renderer(screen)


    # Control the application frame rate
    clock = pygame.time.Clock()

    # Main application loop  
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False


        # draw the grid 
        renderer.draw(grid)

        # Update the display
        pygame.display.flip()

        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
     main()