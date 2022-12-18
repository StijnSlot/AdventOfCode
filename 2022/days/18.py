from util import aoc
from collections import deque


_dd = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), ]


def bfs(grid: list[list[list[bool]]], start: tuple[int, int, int], visited: set[tuple[int, int, int]]):
    Q = deque()
    Q.append(start)
    while len(Q) > 0:
        x = Q.popleft()
        for dx in _dd:
            new_x = (x[0]+dx[0], x[1]+dx[1], x[2]+dx[2])
            if new_x in visited:
                continue
            if not (0 < new_x[0] < len(grid) - 1 and 0 < new_x[1] < len(grid[0]) - 1 and 0 < new_x[2] < len(grid[0][0]) - 1):
                continue
            if grid[new_x[0]][new_x[1]][new_x[2]]:
                continue
            visited.add(new_x)
            Q.append(new_x)


def read_line(line: str) -> tuple[int, int, int]:
    x, y, z = line.split(',')
    return int(x) + 2, int(y) + 2, int(z) + 2  # offset for easier boundaries


def create_grid(data: str) -> list[list[list[bool]]]:
    lines = [read_line(line) for line in data.splitlines()]
    max_d = max(max(x, y, z) + 2 for x, y, z in lines)
    grid = [[[False for _ in range(max_d)] for _ in range(max_d)] for _ in range(max_d)]
    for x, y, z in lines:
        grid[x][y][z] = True
    return grid


def part_one(data: str) -> int:
    grid = create_grid(data)
    return sum(sum(1 for di, dj, dk in _dd if grid[i+di][j+dj][k+dk])
               for i in range(len(grid) - 2)
               for j in range(len(grid[i]) - 2)
               for k in range(len(grid[i][j]) - 2)
               if not grid[i][j][k])


def part_two(data: str) -> int:
    grid = create_grid(data)
    visited = set()
    bfs(grid, (1, 1, 1), visited)
    return sum(1 for i, j, k in visited for di, dj, dk in _dd if grid[i+di][j+dj][k+dk])


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 18)
    print(part_one(input_data))
    print(part_two(input_data))
