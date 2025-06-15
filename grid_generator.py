import random

def generate_random_grid(rows, cols, obstacle_ratio=0.2):
    return [
        [
            1 if random.random() < obstacle_ratio else 0
            for _ in range(cols)
        ]
        for _ in range(rows)
    ]
