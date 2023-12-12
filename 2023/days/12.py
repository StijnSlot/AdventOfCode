from util import aoc
from functools import cache


@cache
def arrangements(springs: tuple[chr], groups: tuple[int], i: int, j: int):
    if j >= len(groups):
        return 1 if all(c != '#' for c in springs[i:]) else 0
    if i >= len(springs):
        return 0
    if sum(groups[j:]) + len(groups) - j - 1 > len(springs) - i:
        return 0
    nr_of_arrangements = 0
    group_end = i + groups[j]
    if all(springs[k] != '.' for k in range(i, group_end)) \
            and (group_end == len(springs) or springs[group_end] != '#'):
        nr_of_arrangements += arrangements(springs, groups, group_end + 1, j + 1)
    if springs[i] != '#':
        k = i + 1
        while k < len(springs) and springs[k] == '.':
            k += 1
        nr_of_arrangements += arrangements(springs, groups, k, j)
    return nr_of_arrangements


def arrangements_for_line(line: str, copies: int = 1) -> int:
    springs_str, groups_str = line.split()
    springs = tuple('?'.join([springs_str] * copies))
    groups = tuple(int(x) for x in groups_str.split(',') * copies)
    return arrangements(springs, groups, 0, 0)


def part_one(data: str) -> int:
    return sum(arrangements_for_line(line) for line in data.splitlines())


def part_two(data: str) -> int:
    return sum(arrangements_for_line(line, 5) for line in data.splitlines())


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 12)
    print(part_one(input_data))
    print(part_two(input_data))
