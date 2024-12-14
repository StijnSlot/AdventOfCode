from util import aoc
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def read_robots(data: str):
    robots = []
    for line in data.splitlines():
        groups = re.match("p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)", line).groups()
        robots.append((Point(int(groups[0]), int(groups[1])), Point(int(groups[2]), int(groups[3]))))
    return robots


def part_one(data: str) -> int:
    robots = read_robots(data)
    width, height = 101, 103
    tl, tr, bl, br = 0, 0, 0, 0
    for p, v in robots:
        p100 = Point((p.x + 100 * v.x) % width, (p.y + 100 * v.y) % height)
        if p100.x < width // 2:
            if p100.y < height // 2:
                tl += 1
            elif p100.y > height // 2:
                bl += 1
        elif p100.x > width // 2:
            if p100.y < height // 2:
                tr += 1
            elif p100.y > height // 2:
                br += 1
    return tl * tr * bl * br


def part_two(data: str) -> int:
    robots = read_robots(data)
    width, height = 101, 103
    for k in range(98, 100000, 103):
        robots_pos = set()
        for p, v in robots:
            pk = Point((p.x + k * v.x) % width, (p.y + k * v.y) % height)
            robots_pos.add(pk)
        # tree gets drawn on right side, check whether most robots are there
        if sum(1 for p in robots_pos if p.x > width // 2 - 10) > 2 * len(robots) // 3:
            return k
    return -1


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 14)
    print(part_one(input_data))
    print(part_two(input_data))
