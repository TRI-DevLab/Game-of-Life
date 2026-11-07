import unittest
import sys
import os

# Ensure the simulation module can be imported from parent directory 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from simulation import create_grid, count_live_neighbors, next_generation

# Test Game of Life simulation

# What we are testing:
# - Empty Grid
# - Under Population 
# - Over Population
# - Reproduction
# - Survival
# - Blinker (Oscillation)
# - That the original grid isn't modified 
# - Block (Still Life)


class TestGameOfLife(unittest.TestCase):

    def test_empty_grid(self):
        """Testing that the created grid that is used to produce the next generation values is initially empty (only has dead cells) once created."""

        grid = create_grid(3, 3)

        # assert that the number of live neighbors of the cell (1, 1) is equal to 0
        self.assertEqual(count_live_neighbors(grid, 1, 1), 0)

        # asset that the next generation of the grid is equal to the previous generation
        self.assertEqual(next_generation(grid), grid)


    def test_under_population(self):
        """Tests the rule that a single live cell that has 0 live neighbors should die in the next generation."""

        grid = create_grid(3, 3)

        # make one cell living 
        grid[1][1] = 1

        # Assign the next generation's grid to a variable
        next_grid = next_generation(grid)

        # Check if the cell that was perviously made living is still alive by asserting if it equal to 0
        self.assertEqual(next_grid[1][1], 0)


    def test_over_population(self):
        """Tests the rule that a center live cell with 4 live neighbors should die in the next generation."""

        grid = create_grid(3, 3)

        # x = column y = row

        # The cell is (1, 1)
        grid[1][1] = 1

        # The neighbors are cells -> [(1, 0), (1, 2), (0, 1), (2, 1)]
        grid[0][1] = 1
        grid[2][1] = 1
        grid[1][0] = 1
        grid[1][2] = 1

        # Assign the next generation's grid to a variable 
        next_grid = next_generation(grid)

        # Check if the cell that was previously made living is still alive by asserting if it equal to 0.
        self.assertEqual(next_grid[1][1], 0)


    def test_reproduction(self):
        """Tests the rule that a dead cell with exactly three live neighbors should become alive in the next generation."""

        grid = create_grid(3, 3)

        # giving cell (1, 1) three live neighbors in hopes that it become alive in the next generation.

        grid[0][1] = 1
        grid[1][0] = 1
        grid[1][2] = 1

        # Assign the next generations's grid to a variable 
        next_grid = next_generation(grid)

        # Check if the cell that was perviously dead has become alive in the next generation.
        self.assertEqual(next_grid[1][1], 1)


    def test_survival(self):
        """Tests the rule that a living cell that has exactly 2 neighbors should survive the next generation."""

        grid = create_grid(3, 3)

        # The cell is (1, 1)
        grid[1][1] = 1

        # The neighbors are (1, 0) and (0, 1)
        grid[0][1] = 1
        grid[1][0] = 1

        # Assign the next generation's grid to a variable 
        next_grid = next_generation(grid)

        # Check if the cell that was previously mad living is still alive in the next generation.
        self.assertEqual(next_grid[1][1], 1)


    def test_blinker_oscillator(self):

        grid = create_grid(5, 5)

        # Generation 0 Horizontal Blinker - make 3 cells live
        grid[2][1] = 1
        grid[2][2] = 1
        grid[2][3] = 1

        # ----- First generation -----
        gen1 = next_generation(grid)

        # Should be Vertical:
        # - check that the 2 cells (2, 1) and (2, 3) that were dead in the previous generation are alive in this generation
        # - check that the cell (2, 2) that was alive in the previous generation is still alive
        self.assertEqual(gen1[1][2], 1)
        self.assertEqual(gen1[2][2], 1)
        self.assertEqual(gen1[3][2], 1)
        # - check that these cells that were alive in the previous generation are dead in this generation
        self.assertEqual(gen1[2][1], 0)
        self.assertEqual(gen1[2][3], 0)

        # ----- Second generation -----
        gen2 = next_generation(gen1)

        # check that it returns to original horizontal state
        self.assertEqual(gen2, grid)


    def test_original_grid_unchanged(self):
        """Test that the original grid isn't modified."""

        grid = create_grid(3, 3)

        # Make cell (1, 1) alive
        grid[1][1] = 1

        # Create a copy of the grid that will be use to assert if the gris has changed 
        original = [row[:] for row in grid]

        # The new grid is not assigned to a variable as we are testing if the gris has changed
        next_generation(grid)

        # Check if the grid has changed by asserting if the grid is equal to the copy of the original
        self.assertEqual(grid, original)


    def test_block_still_life(self):

        grid = create_grid(4, 4)

        # Create block of live cells on the grid
        grid[1][1] = 1
        grid[1][2] = 1
        grid[2][1] = 1
        grid[2][2] = 1

        # Assign the next generations grid to a variable 
        next_grid = next_generation(grid)

        # Check that the next generations grid is equal to the previous generations grid
        self.assertEqual(next_grid, grid)


if __name__ == "__main__":
    unittest.main()









