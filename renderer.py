import pygame 
import config 

# Moving from standalone functions to Classes that give us room for easy expansion 

class Renderer:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    

    def draw(self, grid: list[list[int]]) -> None:
        """Is used to render the grid background, cells, and grid lines."""

        self.screen.fill(config.BACKGROUND_COLOR)

        self._draw_cells(grid)

        self._draw_grid_lines()


    def _draw_cells(self, grid: list[list[int]]) -> None:
    
        rows = len(grid)
        columns = len(grid[0])
        cell_size = config.CELL_SIZE

        for row in range(rows):
            for column in range(columns):

                # Rectangle position and dimensions 
                rect = pygame.Rect(
                    column * cell_size,             # convert grid x coordinate into pixel x coordinate
                    row * cell_size,                # convert grid y coordinate into pixel y coordinate
                    cell_size,
                    cell_size
                )

                # if the cell is alive - color will change
                if grid[row][column] == 1:
                    color = config.ALIVE_COLOR
                else:
                    color = config.DEAD_COLOR


                # Draw the cell
                pygame.draw.rect(
                    self.screen,
                    color,
                    rect
                )


    def _draw_grid_lines(self) -> None:

        cell_size = config.CELL_SIZE
        width = config.WINDOW_WIDTH
        height = config.WINDOW_HEIGHT

        # Draw vertical lines 
        for x in range(0, width + 1, cell_size):
            pygame.draw.line(
                self.screen,
                config.GRID_LINE_COLOR,
                (x, 0),
                (x, height)
            )

        # Draw horizontal lines
        for y in range(0, height + 1, cell_size):
            pygame.draw.line(
                self.screen,
                config.GRID_LINE_COLOR,
                (0, y),
                (width, y)
            )

