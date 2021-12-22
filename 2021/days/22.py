from util import aoc
from math import prod


class Cube:
    def __init__(self, a: (int, int, int), b: (int, int, int), on: bool = True):
        self.a = a
        self.b = b
        self.on = on

    def intersects(self, other):
        return all(aa <= qq and bb >= pp for aa, bb, pp, qq in zip(self.a, self.b, other.a, other.b))

    def area(self):
        return prod(bb - aa for aa, bb in zip(self.a, self.b))

    @classmethod
    def from_line(cls, line: str):
        def read_range(p_range: str) -> (int, int):
            range_parts = p_range.split('..')
            return int(range_parts[0][2:]), int(range_parts[1])
        first, second = line.split()
        on = first == 'on'
        x, y, z = second.split(',')
        x0, x1 = read_range(x)
        y0, y1 = read_range(y)
        z0, z1 = read_range(z)
        return cls((x0, y0, z0), (x1+1, y1+1, z1+1), on)


def read_data(data: str) -> list[Cube]:
    return [Cube.from_line(line) for line in data.splitlines()]


def cube_difference(cube0: Cube, cube1: Cube) -> list[Cube]:
    if not cube0.intersects(cube1):
        return [cube0]
    cubes = []

    # "top"
    if cube0.a[0] < cube1.a[0]:
        cubes.append(Cube(cube0.a, (cube1.a[0], *cube0.b[1:])))

    # "bottom"
    if cube0.b[0] > cube1.b[0]:
        cubes.append(Cube((cube1.b[0], *cube0.a[1:]), cube0.b))

    # "front" minus top,bottom
    if cube0.a[1] < cube1.a[1]:
        new_a = (max(cube0.a[0], cube1.a[0]), *cube0.a[1:])
        new_b = (min(cube0.b[0], cube1.b[0]), cube1.a[1], cube0.b[2])
        cubes.append(Cube(new_a, new_b))

    # "back" minus top,bottom
    if cube0.b[1] > cube1.b[1]:
        new_a = (max(cube0.a[0], cube1.a[0]), cube1.b[1], cube0.a[2])
        new_b = (min(cube0.b[0], cube1.b[0]), *cube0.b[1:])
        cubes.append(Cube(new_a, new_b))

    # "left" side minus top,bottom,back,front
    if cube0.a[2] < cube1.a[2]:
        new_a = (max(cube0.a[0], cube1.a[0]), max(cube0.a[1], cube1.a[1]), cube0.a[2])
        new_b = (min(cube0.b[0], cube1.b[0]), min(cube0.b[1], cube1.b[1]), cube1.a[2])
        cubes.append(Cube(new_a, new_b))

    # "right" side minus top,bottom,back,front
    if cube0.b[2] > cube1.b[2]:
        new_a = (max(cube0.a[0], cube1.a[0]), max(cube0.a[1], cube1.a[1]), cube1.b[2])
        new_b = (min(cube0.b[0], cube1.b[0]), min(cube0.b[1], cube1.b[1]), cube0.b[2])
        cubes.append(Cube(new_a, new_b))

    return [cube for cube in cubes if cube.area() > 0]


def area_on(cubes: list[Cube]) -> int:
    on_cubes = []
    for cube in cubes:
        on_cubes = [x for on_cube in on_cubes for x in cube_difference(on_cube, cube)]
        if cube.on:
            on_cubes.append(cube)
    return sum(cube.area() for cube in on_cubes)


def part_one(data: str) -> int:
    cubes = read_data(data)
    cubes = [cube for cube in cubes if cube.intersects(Cube((-50, -50, -50), (50, 50, 50)))]
    return area_on(cubes)


def part_two(data: str) -> int:
    cubes = read_data(data)
    return area_on(cubes)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 22)
    print(part_one(input_data))
    print(part_two(input_data))
