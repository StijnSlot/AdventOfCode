from util import aoc
from math import prod


def create_grid(data: str) -> [[chr]]:
    return [[x for x in line] for line in data.splitlines()]


def parse_nr(row: [chr], start_nr_index: int, end_nr_index: int) -> int:
    return int(''.join(row[start_nr_index:end_nr_index]))


def get_number_start_end(row: [chr], j: int) -> (int, int):
    start_nr_index, end_nr_index = j, j+1
    while start_nr_index >= 0 and row[start_nr_index].isdigit():
        start_nr_index -= 1
    while end_nr_index < len(row) and row[end_nr_index].isdigit():
        end_nr_index += 1
    return start_nr_index+1, end_nr_index


def is_symbol(grid: [[chr]], x: int, y: int) -> bool:
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not grid[x][y].isdigit() and not grid[x][y] == '.'


def is_part_nr(grid: [[chr]], i: int, start_nr_index: int, end_nr_index: int) -> bool:
    return any(is_symbol(grid, x, y) for x in range(i-1, i+2) for y in range(start_nr_index-1, end_nr_index+1))


def find_nrs(grid: [[chr]], min_x: int = 0, max_x: int = 999999, min_y: int = 0, max_y: int = 999999) -> {(int, int, int)}:
    return {(i, *get_number_start_end(grid[i], j))
            for i in range(min_x, min(max_x, len(grid)))
            for j in range(min_y, min(max_y, len(grid[0])))
            if grid[i][j].isdigit()}


def part_one(data: str) -> int:
    grid = create_grid(data)
    nrs = find_nrs(grid)
    return sum(parse_nr(grid[x], y, k) for (x, y, k) in nrs if is_part_nr(grid, x, y, k))


def part_two(data: str) -> int:
    grid = create_grid(data)
    gear_coords = [(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == '*']
    gear_sum = 0
    for x, y in gear_coords:
        adj_nrs = find_nrs(grid, x-1, x+2, y-1, y+2)
        if len(adj_nrs) == 2:
            gear_sum += prod(parse_nr(grid[a], b, c) for a, b, c in adj_nrs)
    return gear_sum


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 3)
    print(part_one(input_data))
    print(part_two(input_data))
