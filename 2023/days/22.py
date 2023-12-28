from util import aoc
from dataclasses import dataclass, field
from functools import total_ordering

@dataclass
class Point:
    x: int
    y: int
    z: int

@dataclass
@total_ordering
class Cube:
    bottom_left: Point
    top_right: Point
    rest_z: int = None
    rests_on: {int} = field(default_factory=set)
    supports: {int} = field(default_factory=set)

    def __lt__(self, other):
        if self == other:
            return False
        return self.top_right.z < other.top_right.z

    def height(self):
        return self.top_right.z - self.bottom_left.z

    def overlaps_xy(self, other):
        return not (self.top_right.x < other.bottom_left.x
             or self.bottom_left.x > other.top_right.x
             or self.top_right.y < other.bottom_left.y
             or self.bottom_left.y > other.top_right.y)


def parse_cubes(data: str) -> [Cube]:
    return sorted([Cube(*tuple(Point(*tuple(int(x) for x in p.split(','))) for p in line.split('~')))
                   for line in data.splitlines()])


def fall_bricks(cubes: [Cube]) -> None:
    for i, cube in enumerate(cubes):
        rest_z = 1
        rests_on = set()
        for j, stat_cube in enumerate(cubes[:i]):
            if cube.overlaps_xy(stat_cube):
                new_rest_z = stat_cube.rest_z + stat_cube.height() + 1
                if new_rest_z == rest_z:
                    rests_on.add(j)
                elif new_rest_z > rest_z:
                    rest_z = new_rest_z
                    rests_on = {j}
        cube.rest_z = rest_z
        cube.rests_on = rests_on
        for j in rests_on:
            cubes[j].supports.add(i)


def fall_count(cubes: [Cube], i: int) -> int:
    queue = [i]
    fell = {i}
    count = -1
    while queue:
        j = queue.pop(0)
        count += 1
        fell.add(j)
        for k in cubes[j].supports:
            if not cubes[k].rests_on - fell:
                queue.append(k)
    return count


def part_one(data: str) -> int:
    cubes = parse_cubes(data)
    fall_bricks(cubes)
    return sum(1 for i in range(len(cubes)) if all(cube.rests_on != {i} for j, cube in enumerate(cubes) if i != j))


def part_two(data: str) -> int:
    cubes = parse_cubes(data)
    fall_bricks(cubes)
    return sum(fall_count(cubes, i) for i in range(len(cubes)))




if __name__ == "__main__":
    input_data = aoc.get_input(2023, 22)
    print(part_one(input_data))
    print(part_two(input_data))
