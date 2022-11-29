from typing import Callable
from util import aoc


def get_digits(data: str,
               is_allowed_pos: Callable[[int, int], bool],
               pos_map: list[list[str]],
               start: [int, int] = (1, 1)) -> str:
    x, y = start
    dirs = {'U': (0, -1), 'L': (-1, 0), 'D': (0, 1), 'R': (1, 0)}
    result = ""
    for line in data.splitlines():
        for c in line:
            dx, dy = dirs[c]
            if is_allowed_pos(x + dx, y + dy):
                x += dx
                y += dy
        result += pos_map[y][x]
    return result


def part_one(data: str) -> str:
    pos_map = [[str(j + i * 3 + 1) for j in range(3)] for i in range(3)]
    return get_digits(data, lambda x, y: 0 <= x <= 2 and 0 <= y <= 2, pos_map)


def part_two(data: str) -> str:
    pos_map = [[' ', ' ', '1', ' ', ' '],
               [' ', '2', '3', '4', ' '],
               ['5', '6', '7', '8', '9'],
               [' ', 'A', 'B', 'C', ' '],
               [' ', ' ', 'D', ' ', ' ']]
    return get_digits(data, lambda x, y: abs(x - 2) + abs(y - 2) <= 2, pos_map, start=(0, 2))


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 2)
    print(part_one(input_data))
    print(part_two(input_data))
