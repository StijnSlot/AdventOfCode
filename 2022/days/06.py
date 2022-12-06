from util import aoc


def start_of_marker(data: str, x: int) -> int:
    for i in range(len(data) - x):
        if len(set(data[i:i+x])) == x:
            return i + x
    return -1


def part_one(data: str) -> int:
    return start_of_marker(data, 4)


def part_two(data: str) -> int:
    return start_of_marker(data, 14)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 6)
    print(part_one(input_data))
    print(part_two(input_data))
