from util import aoc
from functools import lru_cache


def read_data(data: str) -> (tuple[str], [str]):
    p1, p2 = data.split('\n\n')
    return tuple(str(x.strip()) for x in p1.split(',')), p2.splitlines()


@lru_cache(maxsize=None)
def nr_arrangements(design: str, i: int, towels: tuple[str]) -> int:
    if i >= len(design):
        return 1
    if len(towels) <= 0:
        return 0
    return sum(nr_arrangements(design, i + len(towel), towels)
               for towel in towels
               if design.startswith(towel, i))


def part_one(data: str) -> int:
    towels, designs = read_data(data)
    return sum(1 for design in designs if nr_arrangements(design, 0, towels) > 0)


def part_two(data: str) -> int:
    towels, designs = read_data(data)
    return sum(nr_arrangements(design, 0, towels) for design in designs)


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 19)
    print(part_one(input_data))
    print(part_two(input_data))
