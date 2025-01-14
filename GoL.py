import time
import os

def create_grid(rows, cols):
    grid = [[" " for _ in range(cols)] for _ in range(rows)]

    # Position centrale
    center_row, center_col = rows // 4, cols // 4

    # Ajouter un glider (structure mobile)
    grid[center_row][center_col + 1] = "#"
    grid[center_row + 1][center_col + 2] = "#"
    grid[center_row + 2][center_col] = "#"
    grid[center_row + 2][center_col + 1] = "#"
    grid[center_row + 2][center_col + 2] = "#"

    return grid

def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Effacer l'écran
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print("\n")

def check_neighbors(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    live_neighbors = 0

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "#":
            live_neighbors += 1

    return live_neighbors

def update_grid(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[" " for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbors = check_neighbors(grid, row, col)

            if grid[row][col] == "#" and live_neighbors in [2, 3]:
                new_grid[row][col] = "#"
            elif grid[row][col] == " " and live_neighbors == 3:
                new_grid[row][col] = "#"
            else:
                new_grid[row][col] = " "

    return new_grid

rows, cols = 10, 10  # Taille de la grille
grid = create_grid(rows, cols)

generations = 25
for gen in range(generations):
    print(f"Generation {gen + 1}:")
    display_grid(grid)
    grid = update_grid(grid)
    time.sleep(0.5)  # Ajouter un délai pour visualiser les changements
