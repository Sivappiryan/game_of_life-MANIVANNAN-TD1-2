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
    count = 0
    rows, cols = len(grid), len(grid[0])
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "#":
            count += 1
    return count

def next_generation(grid):
    """Generate the next state of the grid based on the rules."""
    rows, cols = len(grid), len(grid[0])
    new_grid = create_grid(rows, cols)

    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == "#":
                # Cell is alive
                if live_neighbors in [2, 3]:
                    new_grid[x][y] = "#"
                else:
                    new_grid[x][y] = " "
            else:
                # Cell is dead
                if live_neighbors == 3:
                    new_grid[x][y] = "#"

    return new_grid

def main():
    rows, cols = 20, 40  # Dimensions of the grid
    grid = create_grid(rows, cols)

    # Define an initial pattern (glider example)
    grid[1][2] = "#"
    grid[2][3] = "#"
    grid[3][1] = "#"
    grid[3][2] = "#"
    grid[3][3] = "#"

    while True:
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)  # Pause between generations

if __name__ == "__main__":
    main()
