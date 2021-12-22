from util import aoc


def part_one(data: str) -> int:
    data_rows = [int(x) for x in data.splitlines()]
    return sum(1 for i, x in enumerate(data_rows) if i < len(data_rows) - 1 and x < data_rows[i+1])


def part_two(data: str) -> int:
    data_rows = [int(x) for x in data.splitlines()]
    return sum(1 for i, x in enumerate(data_rows) if i < len(data_rows) - 4 and x < data_rows[i+3])


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 1)
    print(part_one(input_data))
    print(part_two(input_data))
