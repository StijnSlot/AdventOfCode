from adventofcode.util import aoc


def part_one(data: str) -> int:
    data_rows = [int(x) for x in data.splitlines()]
    return sum(1 for i in range(len(data_rows) - 1) if data_rows[i] < data_rows[i+1])


def part_two(data: str) -> int:
    data_rows = [int(x) for x in data.splitlines()]
    return sum(1 for i in range(len(data_rows) - 3) if data_rows[i] < data_rows[i+3])


if __name__ == "__main__":
    input_data = aoc.get_input(1)
    print(part_one(input_data))
    print(part_two(input_data))
