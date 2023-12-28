from util import aoc
from enum import Enum
import re
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class Dir(Enum):
    R = (1, 0)
    D = (0, 1)
    L = (-1, 0)
    U = (0, -1)


dir_map = [Dir.R, Dir.D, Dir.L, Dir.U]


def read_trench(data: str, use_color: bool = False) -> [Point]:
    trench = []
    x, y = 0, 0
    for line in data.splitlines():
        match = re.match('(\w) (\d+) \(#(\w+)\)', line)
        dir, k, c = Dir[match.group(1)], int(match.group(2)), match.group(3)
        if use_color:
            k = int(c[:-1], 16)
            dir = dir_map[int(c[-1])]
        x, y = x + k * dir.value[0], y + k * dir.value[1]
        trench.append(Point(x, y))
    return trench


def shoelace(trench):
    area = 0
    for i, p0 in enumerate(trench):
        p1 = trench[(i+1) % len(trench)]
        area += p0.x * p1.y - p0.y * p1.x + abs(p1.x - p0.x + p1.y - p0.y)
    return abs(area // 2) + 1


def part_one(data: str) -> int:
    trench = read_trench(data)
    return shoelace(trench)


def part_two(data: str) -> int:
    trench = read_trench(data, True)
    return shoelace(trench)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 18)
    print(part_one(input_data))
    print(part_two(input_data))
