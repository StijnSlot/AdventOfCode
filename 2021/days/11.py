from util import aoc


def read_grid(data: str) -> list[list[int]]:
    return [[int(x) for x in row] for row in data.splitlines()]


def flash(grid: list[list[int]], i: int, j: int) -> int:
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]
    flashes = 1
    grid[i][j] = 0
    for k in range(len(dx)):
        x, y = i + dx[k], j + dy[k]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0:
            grid[x][y] += 1
            if grid[x][y] > 9:
                flashes += flash(grid, x, y)
    return flashes


def perform_step(grid: list[list[int]]):
    grid = [[x + 1 for x in row] for row in grid]
    flashes = sum(flash(grid, i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] > 9)
    return grid, flashes


def part_one(data: str) -> int:
    grid, ans = read_grid(data), 0
    for _ in range(100):
        grid, flashes = perform_step(grid)
        ans += flashes
    return ans


def part_two(data: str) -> int:
    grid, flashes, steps = read_grid(data), -1, 0
    while flashes != 100:
        grid, flashes = perform_step(grid)
        steps += 1
    return steps


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 11)
    print(part_one(input_data))
    print(part_two(input_data))
