from util import aoc
from functools import cmp_to_key


_start_divider = [['2']]
_end_divider = [['6']]


def parse(line, i=1):
    items = []
    item = ""
    while i <= len(line):
        x = line[i]
        if x == '[':
            item, i = parse(line, i+1)
            items.append(item)
            i += 1
            continue
        elif x == ']':
            if item != "":
                items.append(item)
            return items, i
        if x == ',':
            items.append(item)
            item = ""
        else:
            item += x
        i += 1
    raise ValueError("Line did not correctly parse")


def right_order(items1, items2):
    if items1 == items2:
        return 0
    if type(items1) != list and type(items2) != list:
        return 1 if int(items1) <= int(items2) else -1
    if type(items1) != list:
        return right_order([items1], items2)
    if type(items2) != list:
        return right_order(items1, [items2])
    for x, y in zip(items1, items2):
        a = right_order(x, y)
        if a > 0:
            return 1
        if a < 0:
            return -1
    return 1 if len(items1) < len(items2) else -1 if len(items1) > len(items2) else 0


def part_one(data: str) -> int:
    pairs = [tuple(parse(line)[0] for line in pairs.splitlines()) for pairs in data.split('\n\n')]
    return sum(i + 1 for i, (x, y) in enumerate(pairs) if right_order(x, y) > 0)


def part_two(data: str) -> int:
    lines = [_start_divider] + \
            [parse(line)[0] for pairs in data.split('\n\n') for line in pairs.splitlines()] + \
            [_end_divider]
    lines.sort(key=cmp_to_key(right_order), reverse=True)
    i = lines.index(_start_divider) + 1
    j = lines.index(_end_divider) + 1
    return i * j


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 13)
    print(part_one(input_data))
    print(part_two(input_data))
