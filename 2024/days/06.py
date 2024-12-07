from util import aoc


DD = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_data(data: str) -> ([[chr]], int, int):
    grid = [[c for c in line] for line in data.splitlines()]
    start_i, start_j = next((i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == '^')
    grid[start_i][start_j] = '.'
    return grid, start_i, start_j


def step(grid: [[chr]], i: int, j: int, d: int) -> (int, int, int):
    di, dj = DD[d]
    new_i, new_j = i + di, j + dj
    while 0 <= new_i < len(grid) \
            and 0 <= new_j < len(grid[0]) \
            and grid[new_i][new_j] == '#':
        d = (d + 1) % len(DD)
        di, dj = DD[d]
        new_i, new_j = i + di, j + dj
    return new_i, new_j, d


def calc_visited(grid: [[chr]], start_i: int, start_j: int) -> (int, int, int):
    i, j, d = start_i, start_j, 0
    visited = {i: set() for i in range(len(DD))}  # store map of direction for position
    while 0 <= i < len(grid) and 0 <= j < len(grid[i]):
        if (i, j) in visited[d]:
            return -1, None  # we are in a loop
        visited[d].add((i, j))
        i, j, d = step(grid, i, j, d)
    visited = {p for x in visited for p in visited[x]}  # convert to simple set of positions
    return len(visited), visited


def has_loop(grid: [[chr]], start_i: int, start_j: int, i: int, j: int) -> bool:
    grid[i][j] = '#'
    result, _ = calc_visited(grid, start_i, start_j)
    grid[i][j] = '.'
    return result == -1


def part_one(data: str) -> int:
    grid, start_i, start_j = read_data(data)
    return calc_visited(grid, start_i, start_j)[0]


def part_two(data: str) -> int:
    grid, start_i, start_j = read_data(data)
    _, visited = calc_visited(grid, start_i, start_j)
    return sum(1 for i, j in visited
               if (i, j) != (start_i, start_j) and grid[i][j] == '.' and has_loop(grid, start_i, start_j, i, j))


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 6)
    print(part_one(input_data))
    print(part_two(input_data))
