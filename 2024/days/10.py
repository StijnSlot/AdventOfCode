from util import aoc
from collections import deque

DD = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def trailheads(grid, start_i, start_j):
    Q = deque()
    Q.append((start_i, start_j))
    nines, trails = set(), 0
    while len(Q) > 0:
        i, j = Q.popleft()
        x = grid[i][j]
        if x == 9:
            nines.add((i, j))
            trails += 1
            continue
        for di, dj in DD:
            newi, newj = i + di, j + dj
            if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and grid[newi][newj] == x + 1:
                Q.append((newi, newj))
    return len(nines), trails


def part_one(data: str) -> int:
    grid = [[int(c) for c in line] for line in data.splitlines()]
    return sum(trailheads(grid, i, j)[0] for i, row in enumerate(grid) for j, x in enumerate(row) if x == 0)


def part_two(data: str) -> int:
    grid = [[int(c) for c in line] for line in data.splitlines()]
    return sum(trailheads(grid, i, j)[1] for i, row in enumerate(grid) for j, x in enumerate(row) if x == 0)


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 10)
    print(part_one(input_data))
    print(part_two(input_data))
