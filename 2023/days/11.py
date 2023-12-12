from util import aoc


def parse_grid(data: str) -> ([(int, int)], [int], [int]):
    grid = [[x for x in line] for line in data.splitlines()]
    galaxies = [(x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '#']
    empty_rows = [-1] + [y for y in range(len(grid)) if all(grid[y][x] == '.' for x in range(len(grid[y])))] + [len(grid)]
    empty_columns = [-1] + [x for x in range(len(grid[0])) if all(grid[y][x] == '.' for y in range(len(grid)))] + [len(grid[0])]
    return galaxies, empty_rows, empty_columns


def find_index_closest(values: [int], x: int):
    i_min, i_max = 0, len(values)
    while i_min + 1 < i_max:
        i_h = (i_max + i_min) // 2
        if values[i_h] <= x:
            i_min = i_h
        else:
            i_max = i_h
    return i_min


def calc_dis(p1: (int, int), p2: (int, int), empty_rows: [int], empty_columns: [int], empty_row_mult: int = 1):
    manh = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    manh += empty_row_mult * abs(find_index_closest(empty_rows, p1[1]) - find_index_closest(empty_rows, p2[1]))
    manh += empty_row_mult * abs(find_index_closest(empty_columns, p1[0]) - find_index_closest(empty_columns, p2[0]))
    return manh


def part_one(data: str) -> int:
    galaxies, empty_rows, empty_columns = parse_grid(data)
    return sum(calc_dis(p1, p2, empty_rows, empty_columns) for i, p1 in enumerate(galaxies) for j, p2 in enumerate(galaxies) if i <= j)


def part_two(data: str) -> int:
    galaxies, empty_rows, empty_columns = parse_grid(data)
    return sum(calc_dis(p1, p2, empty_rows, empty_columns, 999999) for i, p1 in enumerate(galaxies) for j, p2 in enumerate(galaxies) if i <= j)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 11)
    print(part_one(input_data))
    print(part_two(input_data))
