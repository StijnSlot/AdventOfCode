from util import aoc


def visible(i, j, grid):
    if i == 0 or i + 1 == len(grid) or j == 0 or j + 1 == len(grid[i]):
        return True
    return grid[i][j] > max(grid[k][j] for k in range(0, i))\
           or grid[i][j] > max(grid[k][j] for k in range(i+1, len(grid))) \
           or grid[i][j] > max(grid[i][:j]) \
           or grid[i][j] > max(grid[i][j+1:])


def scene_score_dir(i, j, grid, di, dj):
    x, y = i + di, j + dj
    result = 0
    while 0 <= x < len(grid) and 0 <= y < len(grid[i]):
        result += 1
        if grid[x][y] >= grid[i][j]:
            return result
        x += di
        y += dj
    return result


def scene_score(i, j, grid):
    return scene_score_dir(i, j, grid, 0, 1) \
           * scene_score_dir(i, j, grid, 1, 0) \
           * scene_score_dir(i, j, grid, 0, -1) \
           * scene_score_dir(i, j, grid, -1, 0)


def read_grid(data: str) -> list[list[int]]:
    return [[int(x) for x in line] for line in data.splitlines()]


def part_one(data: str) -> int:
    grid = read_grid(data)
    return sum(1 for i, line in enumerate(grid) for j, _ in enumerate(line) if visible(i, j, grid))


def part_two(data: str) -> int:
    grid = read_grid(data)
    return max(scene_score(i, j, grid) for i, line in enumerate(grid) for j, _ in enumerate(line))


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 8)
    print(part_one(input_data))
    print(part_two(input_data))
