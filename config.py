# This file prevents hard coding numbers across the directory

# ---- --- Important --- ----
# 0 = Dead Cell 
# 1 = Live Cell

# Grid uses two coordinates grid[row][column] (x = column & y = row)
# Pygame uses pixel coordinates (x, y)

# The conversion from grid coordinates to pixel coordinates:
# x = column * cell size
# y = row * cell size

# Example
# cell -> grid[2][3]. with column = 3 | row = 2 | (3, 2) | cell size = 30
# x = (30 * 3 = 90) | y = (2 * 30 = 60) | pixel position (90, 60)

# Window and Grid dimensions 
CELL_SIZE = 20                          # Pixel size of each square cell 
GRID_WIDTH = 50                         # Number of Columns
GRID_HEIGHT = 30                        # Number of rows 

WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH           # 800px
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT         # 600px


FPS = 60                    # maximum rendering frame rate 
SIMULATION_SPEED = 10       # Generation steps per second when running the program


# Color Palette 
BACKGROUND_COLOR = (18, 18, 24)                        # Deep Slate - Background 
GRID_LINE_COLOR = (32, 34, 46)                          # Grid lines - Grey subtle 
ALIVE_COLOR = (0, 220, 130)                             # Green - Living cells 
DEAD_COLOR = (18, 18, 24)                               # Matches background


