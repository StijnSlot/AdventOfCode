from util import aoc
from math import prod


def get_min_possible_cubes(line: str) -> {str: int}:
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    _, sets = line.split(': ')
    game_sets = sets.split('; ')
    for game_set in game_sets:
        parts = game_set.split(', ')
        for part in parts:
            nr_cubes, color = part.split()
            min_cubes[color] = max(min_cubes[color], int(nr_cubes))
    return min_cubes


def possible_game(line: str, expected_cubes: {str, int}) -> bool:
    min_cubes = get_min_possible_cubes(line)
    return all(min_cubes[c] <= x for c, x in expected_cubes.items())


def power(line: str) -> int:
    return prod(get_min_possible_cubes(line).values())


def part_one(data: str) -> int:
    expected_cubes = {"red": 12, "green": 13, "blue": 14}
    return sum(i+1 for i, line in enumerate(data.splitlines()) if possible_game(line, expected_cubes))


def part_two(data: str) -> int:
    return sum(power(line) for line in data.splitlines())


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 2)
    print(part_one(input_data))
    print(part_two(input_data))
