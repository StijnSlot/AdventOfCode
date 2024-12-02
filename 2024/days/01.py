from util import aoc
from collections import Counter


def read_input(data: str) -> tuple[list[int],list[int]]:
    list1, list2 = [], []
    for line in data.splitlines():
        x, y = line.split()
        list1.append(int(x))
        list2.append(int(y))
    return list1, list2


def part_one(data: str) -> int:
    list1, list2 = read_input(data)
    list1.sort()
    list2.sort()
    return sum(abs(y - x) for x, y in zip(list1, list2))


def part_two(data: str) -> int:
    list1, list2 = read_input(data)
    c = Counter(list2)
    return sum(x * c[x] for x in list1)


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 1)
    print(part_one(input_data))
    print(part_two(input_data))
