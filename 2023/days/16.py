from util import aoc
from enum import Enum


class Dir(Enum):
    N = (0, -1)
    S = (0, 1)
    W = (-1, 0)
    E = (1, 0)


def beam(grid: [[chr]], visited: {(int, int, Dir)}, x: int, y: int, dir: Dir) -> None:
    while (x, y, dir) not in visited and 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        visited.add((x, y, dir))
        if grid[y][x] == '/':
            dir = Dir((-dir.value[1], -dir.value[0]))
        elif grid[y][x] == '\\':
            dir = Dir((dir.value[1], dir.value[0]))
        elif grid[y][x] == '-' and dir in (Dir.N, Dir.S):
            beam(grid, visited, x, y, Dir.W)
            dir = Dir.E
        elif grid[y][x] == '|' and dir in (Dir.E, Dir.W):
            beam(grid, visited, x, y, Dir.N)
            dir = Dir.S
        x += dir.value[0]
        y += dir.value[1]


def energizes(grid: [[chr]], startx: int, starty: int, dir: Dir) -> int:
    visited = set()
    beam(grid, visited, startx, starty, dir)
    return len({(x, y) for x, y, _ in visited})


def part_one(data: str) -> int:
    grid = [[c for c in line] for line in data.splitlines()]
    return energizes(grid, 0, 0, Dir.E)


def part_two(data: str) -> int:
    grid = [[c for c in line] for line in data.splitlines()]
    return max(
        max(energizes(grid, 0, i, Dir.E) for i in range(len(grid))),
        max(energizes(grid, len(grid[0]) - 1, i, Dir.W) for i in range(len(grid))),
        max(energizes(grid, i, 0, Dir.S) for i in range(len(grid[0]))),
        max(energizes(grid, i, len(grid) - 1, Dir.N) for i in range(len(grid[0])))
    )


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 16)
    print(part_one(input_data))
    print(part_two(input_data))
