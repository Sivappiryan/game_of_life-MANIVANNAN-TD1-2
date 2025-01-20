import os
import time

def create_grid(rows, cols):
    """Create a grid with all dead cells."""
    return [[" " for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    """Display the grid in the console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print("".join(row))

def count_neighbors(grid, x, y):
    """Count the number of live neighbors around a cell."""
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    rows, cols = len(grid), len(grid[0])
    return sum(
        0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == "#"
        for dx, dy in directions
    )

def next_generation(grid):
    """Generate the next state of the grid based on the rules."""
    rows, cols = len(grid), len(grid[0])
    new_grid = create_grid(rows, cols)

    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == "#" and live_neighbors in [2, 3]:
                new_grid[x][y] = "#"
            elif grid[x][y] == " " and live_neighbors == 3:
                new_grid[x][y] = "#"

    return new_grid

def add_pattern(grid, pattern, x_offset=0, y_offset=0):
    """Add a predefined pattern to the grid at the given offset."""
    for x, row in enumerate(pattern):
        for y, cell in enumerate(row):
            if 0 <= x + x_offset < len(grid) and 0 <= y + y_offset < len(grid[0]):
                grid[x + x_offset][y + y_offset] = cell

def main(rows=20, cols=40, speed=0.5):
    """Main function to run the Game of Life."""
    grid = create_grid(rows, cols)

    # Define an initial pattern (glider example)
    glider = [
        [" ", "#", " "],
        [" ", " ", "#"],
        ["#", "#", "#"]
    ]
    add_pattern(grid, glider, x_offset=1, y_offset=2)

    while True:
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(speed)

if __name__ == "__main__":
    # Dynamic grid size and speed setup
    rows, cols, speed = 20, 40, 0.5
    try:
        rows_input = input("Enter grid rows (default 20): ")
        if rows_input.strip():
            rows = int(rows_input)
        cols_input = input("Enter grid columns (default 40): ")
        if cols_input.strip():
            cols = int(cols_input)
        speed_input = input("Enter speed in seconds (default 0.5): ")
        if speed_input.strip():
            speed = float(speed_input)
    except ValueError:
        print("Invalid input detected! Using default values (rows=20, cols=40, speed=0.5).")

    main(rows, cols, speed)
