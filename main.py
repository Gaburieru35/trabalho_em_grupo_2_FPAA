from flood_fill import flood_fill_all, print_grid
from grid_generator import generate_random_grid
from visualizer import visualize_flood_fill

def main():
    while True:
        grid = generate_random_grid(10, 10, obstacle_ratio=0.3)
        if grid[0][0] == 0:
            break  # Garante que o ponto inicial é navegável

    start_x, start_y = 0, 0

    print("Grid inicial:")
    print_grid(grid)

    updated_grid = visualize_flood_fill(grid, start_x, start_y, flood_fill_all)

    print("\nGrid preenchido:")
    print_grid(updated_grid)

if __name__ == "__main__":
    main()
