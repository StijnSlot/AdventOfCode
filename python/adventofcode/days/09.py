from adventofcode.util import aoc


def neighbours(grid: list[str], i: int, j: int) -> iter:
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    for k in range(len(dx)):
        x, y = i + dx[k], j + dy[k]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            yield x, y


def get_basin_size(grid: list[str], visited: set[(int, int)], i: int, j: int) -> int:
    count = 1
    visited.add((i, j))
    for x, y in neighbours(grid, i, j):
        if (x, y) not in visited and grid[x][y] != '9':
            count += get_basin_size(grid, visited, x, y)
    return count


def part_one(data: str) -> int:
    grid = data.splitlines()
    return sum(1 + int(grid[i][j])
               for i in range(len(grid))
               for j in range(len(grid[0]))
               if all(grid[i][j] < grid[x][y] for x, y in neighbours(grid, i, j)))


def part_two(data: str) -> int:
    grid = data.splitlines()
    visited = set()
    sizes = sorted(get_basin_size(grid, visited, i, j)
                   for i in range(len(grid))
                   for j in range(len(grid[0]))
                   if (i, j) not in visited and grid[i][j] != '9')
    return sizes[-1] * sizes[-2] * sizes[-3]


if __name__ == "__main__":
    input_data = aoc.get_input(9)
    print(part_one(input_data))
    print(part_two(input_data))
