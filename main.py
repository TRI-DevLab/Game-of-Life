import pygame
import sys 
import config
from simulation import create_grid, next_generation, randomize_grid, clear_grid
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

    # Simulation state variables 
    is_running = False
    generation = 0
    speed = config.SIMULATION_SPEED         # Generations per second 
    time_since_last_step = 0

    # Mouse dragging tracking 
    drawing = False
    draw_state = 1

    running = True
    while running:
        dt = clock.tick(config.FPS) / 1000.0                    # Seconds passed since last frame

        for event in pygame.event.get():

            # For exiting program
            if event.type == pygame.QUIT:
                running = False

            # Keyboard Controls
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                             # For pause and play
                    is_running = not is_running

                elif (event.key == pygame.K_s) and (not is_running):        # for next generation
                    grid = next_generation(grid)

                elif event.key == pygame.K_c:                               # Used to clear everything 
                    grid = clear_grid(config.GRID_HEIGHT, config.GRID_WIDTH)
                    generation = 0
                    is_running = False

                elif event.key == pygame.K_r:                               # Add a bunch or randomly placed live cells 
                    grid = randomize_grid(config.GRID_HEIGHT, config.GRID_WIDTH)
                    generation = 0

                elif event.key == pygame.K_UP:                              # for increasing speed
                    speed = min(60, speed + 1)

                elif event.type == pygame.K_DOWN:                           # for decreasing speed
                    speed = max(1, speed - 1)
                

            # Mouse Interaction: Clicking and drag drawing 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):           # left click (draw) and Right click (erase)

                    drawing = False

                    if event.button == 1:
                        draw_state = 1 
                    else:
                        draw_state = 0

                    # get position 
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = mouse_x // config.CELL_SIZE
                    row = mouse_y // config.CELL_SIZE

                    if (0 <= row < config.GRID_HEIGHT) and (0 <= column < config.GRID_WIDTH):
                        grid[row][column] = draw_state

            # Display
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in (1, 3):
                    drawing = False

            if event.type == pygame.MOUSEMOTION and drawing:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                column = mouse_x // config.CELL_SIZE
                row = mouse_y // config.CELL_SIZE

                if (0 <= row < config.GRID_HEIGHT) and (0 <= column < config.GRID_WIDTH):
                    grid[row][column] = draw_state


        if is_running:
            time_since_last_step += dt
            step_interval = 0.1 / speed
            while time_since_last_step >= step_interval:
                grid = next_generation(grid)
                generation += 1
                time_since_last_step -= step_interval

            

        
        # Draw the grid
        renderer.draw(grid, is_running, generation, speed)

        # Update the display
        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()