from util import aoc


def read_data(data: str) -> list[list[tuple[int, int]]]:
    return [[(int(x.split('-')[0]), int(x.split('-')[1])) for x in line.split(',')] for line in data.splitlines()]


def is_contained(x: tuple[int, int], y: tuple[int, int]):
    return y[0] <= x[0] and y[1] >= x[1]


def overlaps(x, y):
    return y[0] <= x[0] <= y[1] or y[0] <= x[1] <= y[1]


def part_one(data: str) -> int:
    ranges = read_data(data)
    return sum(1 for tasks in ranges if any(is_contained(x, y) for x in tasks for y in tasks if x is not y))


def part_two(data: str) -> int:
    ranges = read_data(data)
    return sum(1 for tasks in ranges if any(overlaps(x, y) for x in tasks for y in tasks if x is not y))


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 4)
    print(part_one(input_data))
    print(part_two(input_data))
