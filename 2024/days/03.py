from util import aoc
import re


MUL_REGEX = re.compile(r"mul\((\d+),(\d+)\)")
DO_REGEX = re.compile(r"do\(\)")
DO_NOT_REGEX = re.compile(r"don't\(\)")


def part_one(data: str) -> int:
    return sum(int(x) * int(y) for x, y in MUL_REGEX.findall(data))


def part_two(data: str) -> int:
    enabled, i = True, 0
    result = 0
    while i < len(data):
        end = len(data)
        if enabled:
            match = DO_NOT_REGEX.search(data, pos=i)
            if match is not None:
                end = match.span()[0]
                enabled = False
            result += sum(int(x) * int(y) for x, y in MUL_REGEX.findall(data, pos=i, endpos=end))
        else:
            match = DO_REGEX.search(data, pos=i)
            if match is not None:
                enabled = True
                end = match.span()[0]
        i = end + 1
    return result


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 3)
    print(part_one(input_data))
    print(part_two(input_data))
