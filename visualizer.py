import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

COLOR_LIST = [
    "white", "black", "red", "orange", "yellow", "green",
    "cyan", "blue", "purple", "pink", "brown"
]
cmap = mcolors.ListedColormap(COLOR_LIST)

def show_grid(grid, title=""):
    plt.imshow(grid, cmap=cmap)
    plt.title(title)
    plt.pause(0.3)
    plt.clf()

def visualize_flood_fill(grid, start_x, start_y, flood_fill_all_fn):
    return flood_fill_all_fn(grid, start_x, start_y, visualize=True, show_callback=show_grid)
