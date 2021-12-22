from itertools import combinations
from util import aoc


def sub(p: tuple, q: tuple) -> tuple:
    return tuple(x - y for x, y in zip(p, q))


def add(p: tuple, q: tuple) -> tuple:
    return tuple(x + y for x, y in zip(p, q))


def read_scanners(data: str) -> list[list[(int, int, int)]]:
    return [[tuple(int(c) for c in x.split(',')) for x in scanner.splitlines()[1:]]
            for scanner in data.split('\n\n')]


def orientations24(points: list[tuple]):
    def orient(p: tuple, k: int) -> tuple:
        x, y, z = p
        orientations = [
            (x, y, z), (y, z, x), (z, x, y), (-x, z, y), (z, y, -x), (y, -x, z),
            (z, -y, x), (-y, x, z), (x, z, -y), (y, x, -z), (x, -z, y), (-z, y, x),
            (-x, -y, z), (-y, z, -x), (z, -x, -y), (-x, y, -z), (y, -z, -x), (-z, -x, y),
            (x, -y, -z), (-y, -z, x), (-z, x, -y), (-x, -z, -y), (-z, -y, -x), (-y, -x, -z),

        ]
        return orientations[k]
    return [{orient(p, k) for p in points} for k in range(24)]


def offset(points):
    return {p: {sub(p, q) for q in points} for p in points}


def find_offset(beacons, points, offset_beacons, offset_points):
    for p in beacons:
        for q in points:
            if len(offset_beacons[p].intersection(offset_points[q])) >= 12:
                return sub(p, q)


def match_new_scanners(beacons, orientations, offset_beacons, offsets):
    for points, offset_points in zip(orientations, offsets):
        if result := find_offset(beacons, points, offset_beacons, offset_points):
            return {add(p, result) for p in points}, result


def map_beacons(scanners: list[list[(int, int, int)]]) -> (set[(int, int, int)], set[(int, int, int)]):
    beacons = set(scanners[0])
    remaining = set(range(1, len(scanners)))
    orientations = {i: orientations24(scanners[i]) for i in remaining}
    offsets = {i: [offset(orient) for orient in orientations[i]] for i in remaining}
    locations = {(0, 0, 0)}
    while remaining:
        offset_beacons = offset(beacons)
        for i in remaining:
            if result := match_new_scanners(beacons, orientations[i], offset_beacons, offsets[i]):
                p, off = result
                beacons |= p
                locations.add(off)
                remaining.remove(i)
                break
    return beacons, locations


def part_one(data: str) -> int:
    scanners = read_scanners(data)
    return len(map_beacons(scanners)[0])


def part_two(data: str) -> int:
    scanners = read_scanners(data)
    scan_positions = map_beacons(scanners)[1]
    return max(sum(abs(x - y) for x, y in zip(p, q)) for p, q in combinations(scan_positions, 2))


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 19)
    print(part_one(input_data))
    print(part_two(input_data))
