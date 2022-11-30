from util import aoc
import re


def read_triangles(data: str) -> list[list[int, int, int]]:
    return [[int(x) for x in re.findall("\d+", line)] for line in data.splitlines()]


def valid_triangle(x: int, y: int, z: int) -> bool:
    a, b, c = sorted((x, y, z))
    return a + b > c


def part_one(data: str) -> int:
    triangles = read_triangles(data)
    return sum(1 for (x, y, z) in triangles if valid_triangle(x, y, z))


def part_two(data: str) -> int:
    triangles = read_triangles(data)
    new_triangles = []
    for i in range(0, len(triangles), 3):
        for j in range(3):
            new_triangles.append((triangles[i][j], triangles[i+1][j], triangles[i+2][j]))
    return sum(1 for (x, y, z) in new_triangles if valid_triangle(x, y, z))


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 3)
    print(part_one(input_data))
    print(part_two(input_data))
