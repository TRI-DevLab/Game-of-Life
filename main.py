import pygame
import sys 
import config
from simulation import create_grid
from renderer import Renderer

def main():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")
    # Screen size
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Create the empty grid
    grid = create_grid(config.GRID_HEIGHT, config.GRID_WIDTH)
    # Assign it to render class for display
    renderer = Renderer(screen)

    running = True
    while running:
        for event in pygame.event.get():

            # For exiting program
            if event.type == pygame.QUIT:
                running = False

            # Toggle cell on left mouse click 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:           # left click

                    # get position 
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = mouse_x // config.CELL_SIZE
                    row = mouse_y // config.CELL_SIZE

                    if (0 <= row < config.GRID_HEIGHT) and (0 <= column < config.GRID_WIDTH):
                        if grid[row][column] == 1:
                            grid[row][column] = 0
                        else:
                            grid[row][column] = 1

        # Draw the grid
        renderer.draw(grid)

        # Update the display
        pygame.display.flip()

        # Limit frame rate to 60 FPS
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()