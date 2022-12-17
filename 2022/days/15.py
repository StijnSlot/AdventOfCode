from util import aoc
import re


_re_str = "Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)"
_dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
_max_x = 99999999


def can_be_beacon(sensor_beacons: list[tuple[int, int, int, int]], x: int, y: int):
    found = False
    next_x_beacon = []
    next_x_not_beacon = [_max_x]
    for xs, ys, xb, yb in sensor_beacons:
        dis_to_beacon = abs(xs - xb) + abs(ys - yb)
        dis_to_point = abs(xs - x) + abs(ys - y)
        dif = dis_to_point - dis_to_beacon
        if dif <= 0:
            new_x = x - dif + 1 + (2 * (xs - x) if x < xs else 0)
            found = True
            next_x_beacon.append(new_x)
        elif x < xb:
            next_x_not_beacon.append(x + dif)
    if found:
        return False, max(next_x_beacon)
    return True, min(next_x_not_beacon)


def read_input(data: str) -> list[tuple[int, int, int, int]]:
    sensor_beacons = []
    for line in data.splitlines():
        match = re.match(_re_str, line)
        xs, ys, xb, yb = match.groups()
        sensor_beacons.append((int(xs), int(ys), int(xb), int(yb)))
    return sensor_beacons


def part_one(data: str) -> int:
    sensor_beacons = read_input(data)
    y = 2000000
    result = 0
    x = -_max_x
    while x < _max_x:
        c, new_x = can_be_beacon(sensor_beacons, x, y)
        if c:
            x = new_x
        else:
            result += new_x - x
            if sum(1 for _, _, xb, yb in sensor_beacons if x <= xb < new_x and y == yb):
                # don't count beacons
                result -= 1
            x = new_x
    return result


def part_two(data: str) -> int:
    min_p, max_p = 0, 4000000
    sensor_beacons = read_input(data)
    for y in range(min_p, max_p + 1):
        x = min_p
        while x <= max_p:
            c, new_x = can_be_beacon(sensor_beacons, x, y)
            if c:
                return 4000000 * x + y
            x = new_x


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 15)
    print(part_one(input_data))
    print(part_two(input_data))
