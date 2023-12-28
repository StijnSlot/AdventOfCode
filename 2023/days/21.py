from util import aoc
from enum import Enum


class Dir(Enum):
    U = (0, -1)
    D = (0, 1)
    L = (-1, 0)
    R = (1, 0)


def bfs(grid, start):
    queue = [(0, start)]
    dists = {}
    while queue:
        dis, (x, y) = queue.pop(0)
        if (x, y) in dists:
            continue
        dists[(x, y)] = dis
        for dir in Dir:
            new_x, new_y = x + dir.value[0], y + dir.value[1]
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]) and grid[new_y][new_x] == '.':
                queue.append((dis + 1, (new_x, new_y)))
    return dists


def part_one(data: str) -> int:
    grid = [[c for c in line] for line in data.splitlines()]
    start = next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'S')
    grid[start[1]][start[0]] = '.'
    dists = bfs(grid, start)
    return sum(1 for d in dists.values() if d % 2 == 0 and d <= 64)


def part_two(data: str) -> float:
    grid = [[c for c in line] for line in data.splitlines()]
    start = next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'S')
    grid[start[1]][start[0]] = '.'
    dists = bfs(grid, start)

    even_corners = sum(1 for d in dists.values() if d % 2 == 0 and d > 65)
    odd_corners = sum(1 for d in dists.values() if d % 2 == 1 and d > 65)

    even_full = sum(1 for d in dists.values() if d % 2 == 0)
    odd_full = sum(1 for d in dists.values() if d % 2 == 1)

    n = (26501365 - (len(grid) // 2)) / len(grid)

    return ((n+1)*(n+1)) * odd_full + (n*n) * even_full - (n+1) * odd_corners + n * even_corners


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 21)
    print(part_one(input_data))
    print(part_two(input_data))
