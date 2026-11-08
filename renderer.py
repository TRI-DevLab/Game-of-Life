import pygame 
import config 

# Moving from standalone functions to Classes that give us room for easy expansion 

class Renderer:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont("monospace", 14, bold = True)

    

    def draw(self, grid: list[list[int]], is_running: bool, generation: int, speed: int) -> None:
        """Is used to render the grid background, cells, grid lines, and status HUD."""

        self.screen.fill(config.BACKGROUND_COLOR)

        self._draw_cells(grid)

        self._draw_grid_lines()

        self._draw_hud(is_running, generation, speed)


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


    def _draw_hud(self, is_running: bool, generation: int, speed: int) -> None:

        # Status Display
        if is_running:
            status_text = "RUNNING"
            status_color = (0, 220, 130)
        else:
            status_text = "PAUSED"
            status_color = (220, 80, 80)

        info_string = f"{status_text} | Gen: {generation} | Speed: {speed} gen/s | Controls: [Space] Play/Pause  [S] Next Gen  [R] Random  [C] Clear  [↑/↓] Speed"

        text_surface = self.font.render(info_string, True, (240, 240, 240))
        bg_rect = pygame.Rect(5, 5, text_surface.get_width() + 10, text_surface.get_height() + 6)

        # Translucent dark backing box for readability
        hud_surface = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        hud_surface.fill((10, 10, 15, 200))

        self.screen.blit(hud_surface, (bg_rect.x, bg_rect.y))
        self.screen.blit(text_surface, (bg_rect.x + 5, bg_rect.y + 3))