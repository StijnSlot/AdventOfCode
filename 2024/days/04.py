from util import aoc


DD = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def read_grid(data: str) -> [[chr]]:
    return [c for c in data.splitlines()]


def xmas(grid, i_start, j_start):
    xmas_sum = 0
    for di, dj in DD:
        i, j = i_start, j_start
        word = ''
        for k in range(4):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                break
            word += grid[i][j]
            i += di
            j += dj
        if word == 'XMAS':
            xmas_sum += 1
    return xmas_sum


def xmas2(grid, i_start, j_start):
    if grid[i_start][j_start] != 'A':
        return 0
    if i_start == 0 or i_start == len(grid) - 1 or j_start == 0 or j_start == len(grid[0]) - 1:
        return 0
    return 1 \
        if ['M', 'S'] == sorted(grid[i_start-1][j_start-1] + grid[i_start+1][j_start+1]) \
           and ['M', 'S'] == sorted(grid[i_start+1][j_start-1] + grid[i_start-1][j_start+1]) \
        else 0


def part_one(data: str) -> int:
    grid = read_grid(data)
    return sum(xmas(grid, i, j) for i in range(len(grid)) for j in range(len(grid[0])))


def part_two(data: str) -> int:
    grid = read_grid(data)
    return sum(xmas2(grid, i, j) for i in range(len(grid)) for j in range(len(grid[0])))


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 4)
    print(part_one(input_data))
    print(part_two(input_data))
