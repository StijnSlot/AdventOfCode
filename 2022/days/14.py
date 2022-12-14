from util import aoc


_start_x, _start_y = 500, 0


def simulate_sand(grid, startx, starty):
    x, y = startx, starty
    rest = 0
    while y + 1 < len(grid):
        if grid[y+1][x] == '.':
            y += 1
        elif grid[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif grid[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            # rest
            grid[y][x] = '+'
            rest += 1
            x, y = startx, starty
            if grid[y][x] != '.':
                return rest
    return rest


def parse_lines(data: str) -> list[list[tuple[int, ...]]]:
    return [[tuple(int(x) for x in coord.split(',')) for coord in line.split(' -> ')] for line in data.splitlines()]


def create_grid(lines: list[list[tuple[int, ...]]], add_floor: bool) -> list[list[str]]:
    max_y = max(x[1] for line in lines for x in line)
    max_x = max(x[0] for line in lines for x in line)
    grid = [['.' for _ in range(2 * max_x)] for _ in range(max_y + 2)]
    if add_floor:
        grid.append(['#' for _ in range(2 * max_x)])
    for line in lines:
        x, y = line[0]
        for new_x, new_y in line[1:]:
            grid[y][x] = '#'
            dx = (new_x - x) // abs(new_x - x) if new_x != x else 0
            dy = (new_y - y) // abs(new_y - y) if new_y != y else 0
            while x != new_x or y != new_y:
                x += dx
                y += dy
                grid[y][x] = '#'
    return grid


def part_one(data: str) -> int:
    lines = parse_lines(data)
    grid = create_grid(lines, False)
    return simulate_sand(grid, _start_x, _start_y)


def part_two(data: str) -> int:
    lines = parse_lines(data)
    grid = create_grid(lines, True)
    return simulate_sand(grid, _start_x, _start_y)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 14)
    print(part_one(input_data))
    print(part_two(input_data))
