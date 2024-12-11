from util import aoc
from itertools import combinations
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def read_data(data: str) -> ([[chr]], {chr: [Point]}):
    grid = [[c for c in line] for line in data.splitlines()]
    antennas = {cell for row in grid for cell in row if cell != '.'}
    antennas_pos = {a: [Point(j, i) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == a]
                    for a in antennas}
    return grid, antennas_pos


def in_bounds(p: Point, grid: [[chr]]) -> bool:
    return 0 <= p.x < len(grid[0]) and 0 <= p.y < len(grid)


def part_one(data: str) -> int:
    grid, antennas_pos = read_data(data)
    antinodes = set()
    for a in antennas_pos:
        for a1, a2 in combinations(antennas_pos[a], 2):
            dx = a2.x - a1.x
            dy = a2.y - a1.y
            ant1 = Point(a1.x - dx, a1.y - dy)
            if in_bounds(ant1, grid):
                antinodes.add(ant1)
            ant2 = Point(a1.x + 2 * dx, a1.y + 2 * dy)
            if in_bounds(ant2, grid):
                antinodes.add(ant2)
    return len(antinodes)


def part_two(data: str) -> int:
    grid, antennas_pos = read_data(data)
    antinodes = set()
    for a in antennas_pos:
        for a1, a2 in combinations(antennas_pos[a], 2):
            dx = a2.x - a1.x
            dy = a2.y - a1.y
            divisor = gcd(dx, dy)
            dx /= divisor
            dy /= divisor
            p = a1
            while in_bounds(p, grid):
                antinodes.add(p)
                p = Point(p.x - dx, p.y - dy)
            p = a1
            while in_bounds(p, grid):
                antinodes.add(p)
                p = Point(p.x + dx, p.y + dy)
    return len(antinodes)


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 8)
    print(part_one(input_data))
    print(part_two(input_data))
