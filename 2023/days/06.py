from util import aoc
from math import prod


def parse_data(data: str, remove_spaces: bool = False) -> [(int, int)]:
    lines = data.replace(" ", "").replace(":", " ").splitlines() if remove_spaces else data.splitlines()
    times = [int(x) for x in lines[0].split()[1:]]
    dists = [int(x) for x in lines[1].split()[1:]]
    return [x for x in zip(times, dists)]


def is_possible(time: int, best_dist: int, wait_time: int) -> bool:
    return (time - wait_time) * wait_time > best_dist


def possible_ways(time: int, best_dist: int) -> int:
    return sum(1 for i in range(1, time) if is_possible(time, best_dist, i))


def part_one(data: str) -> int:
    input_data = parse_data(data)
    return prod(possible_ways(x, y) for x, y in input_data)


def part_two(data: str) -> int:
    time, best_dist = parse_data(data, True)[0]
    x_min, x_max = 0, time // 2
    while x_min + 1 < x_max:
        x_half = (x_min + x_max) // 2
        if is_possible(time, best_dist, x_half):
            x_max = x_half
        else:
            x_min = x_half
    y_min, y_max = time // 2, time
    while y_min + 1 < y_max:
        y_half = (y_min + y_max) // 2
        if is_possible(time, best_dist, y_half):
            y_min = y_half
        else:
            y_max = y_half
    return y_max - x_max


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 6)
    print(part_one(input_data))
    print(part_two(input_data))
