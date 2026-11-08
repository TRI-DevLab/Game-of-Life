# --- ---- Simulation of Game of Life ---- ---

# 1 = Alive
# 0 = Dead

# Creating Grid -> grid[Row][Column]

def create_grid(rows: int, columns: int) -> list[list[int]]:
    """Creates an empty grid populated entirely with dead cells (0)."""

    # Error handling 
    if rows <= 0 or columns <= 0:
        raise ValueError("Grid dimensions must be positive")

    return [[0 for _ in range(columns)] for _ in range(rows)]




# Neighbor counting algorithm for each item - counts which neighbors are live for each cell

# every cell has eight possible neighbors 
neighbor_offset = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

# The wrap allows:
# - the top edge to connect to the bottom edge 
# - and the right edge to connect to the left 
# - for a continuous neighbor 

def count_live_neighbors(grid: list[list[int]], row: int, column: int, wrap = False) -> int:
    """Counts the number of living neighbors around grid[row][col]."""

    rows = len(grid)                        # stores number of rows in a grid
    columns = len(grid[0])                  # stores the number of columns for a row

    live_neighbors = 0                      # neighbor counter

    for row_offset, column_offset in neighbor_offset:           # iterate through the possible neighbor options 

        neighbor_row = row + row_offset                         # add to actual cell row to create neighbor cell row
        neighbor_column = column + column_offset                # add to actual cell column to create neighbor cell column

        if wrap:                                                # for cells at the edge of a grid to have a continuous neighbor 

            neighbor_row = neighbor_row % rows                                      # helps wrap the grid and move the neighbor cell to the edge row to continue the search for live cells (instead of it having limited neighbors)
            neighbor_column = neighbor_column % columns                             # helps warp the gird and move the neighbor cell to the edge column to continue the search for live cells 

            if grid[neighbor_row][neighbor_column] == 1:
                live_neighbors += 1

        else:                                                   # not wrapped so it has to confine to the boundary

            if (0 <= neighbor_row < rows) and (0 <= neighbor_column < columns):         # if it is in bounds move on

                if grid[neighbor_row][neighbor_column] == 1:                           # if the cell is equal to 1 meaning alive the counter increases  
                    live_neighbors += 1                                                   


    return live_neighbors


# Rules:
# 1. current state = 1 & living neighbors (1 - 0) -> Next state = 0
# 2. current state = 1 & living neighbors (2 - 3) -> Next state = 1
# 3. current state = 1 & living neighbors (4 - 8) -> Next state = 0
# 4. current state = 0 & living neighbors (3) -> Next state = 1
# 5. current state = 0 & living neighbors (anything else) - Next state = 0


# Creates a new grid with the ne generation of living cells (does not update the grid)

def next_generation(grid: list[list[int]], wrap: bool = False) -> list[list[int]]:
    """Calculates and returns the next generation of the grid."""

    rows = len(grid)
    columns = len(grid[0])


    # Create a new grid containing only dead cells
    new_grid = create_grid(rows, columns)


    # Examine every cell in the current generation.
    for row in range(rows):
        for col in range(columns):

            # Count live neighbors.
            neighbors = count_live_neighbors(grid, row, col, wrap = wrap)

            # Get the current cell's state 
            current_state = grid[row][col]

            # Applying Conway's Rules 
            if current_state == 1:

                if neighbors < 2:
                    new_grid[row][col] = 0

                elif neighbors in (2, 3):
                    new_grid[row][col] = 1

                else:

                    new_grid[row][col] = 0

            else:

                if neighbors == 3:
                    new_grid[row][col] = 1

    return new_grid

def display_grid(grid: list[list[int]]) -> None:
    """Displays the grid using (#) for alive and (.) for dead."""

    for row in grid:
        symbols = []

        for cell in row:
            if cell == 1:
                symbols.append('#')
            else:
                symbols.append('.')

        print(' '.join(symbols))


if __name__ == "__main__":
    # 5x5  grid with a horizontal 3-cell blinker in the center 

    test_grid = create_grid(5, 5)
    test_grid[2][1] = 1
    test_grid[2][2] = 1
    test_grid[2][3] = 1

    # Test Grid
    print("Generation 0 (Horizontal):")
    display_grid(test_grid)

    # Generation 1
    gen_1 = next_generation(test_grid)
    print("\nGeneration 1 (Expected Vertical):")
    display_grid(gen_1)

    # Generation 2
    gen_2 = next_generation(gen_1)
    print('\nGeneration 2 (Expected Horizontal):')
    display_grid(gen_2)

