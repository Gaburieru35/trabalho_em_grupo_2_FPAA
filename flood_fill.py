from collections import deque

# Movimentos: cima, baixo, esquerda, direita
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    return (
        0 <= x < n and 0 <= y < m
        and grid[x][y] == 0
        and not visited[x][y]
    )

def flood_fill(grid, x, y, color, visited, visualize=False, show_callback=None):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    grid[x][y] = color

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            if valid(grid, nx, ny, visited):
                visited[nx][ny] = True
                grid[nx][ny] = color
                queue.append((nx, ny))

                if visualize and show_callback:
                    show_callback(grid, title=f"Preenchendo com cor {color}")

def flood_fill_all(grid, start_x, start_y, visualize=False, show_callback=None):
    n, m = len(grid), len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    color = 2

    # Começa pelo ponto fornecido
    if grid[start_x][start_y] == 0:
        flood_fill(grid, start_x, start_y, color, visited, visualize, show_callback)
        color += 1

    # Preenche as demais regiões automaticamente
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and not visited[i][j]:
                flood_fill(grid, i, j, color, visited, visualize, show_callback)
                color += 1

    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))
