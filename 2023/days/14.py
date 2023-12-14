from util import aoc


def flip(grid: [[chr]]) -> [[chr]]:
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]


def rev_hor(grid: [[chr]]) -> [[chr]]:
    return [row[::-1] for row in grid]


def rot90(grid: [[chr]]) -> [[chr]]:
    return rev_hor(flip(grid))


def rot280(grid: [[chr]]) -> [[chr]]:
    return flip(rev_hor(grid))


def tilt_left(grid: [[chr]]) -> [[chr]]:
    rows = []
    for row in grid:
        new_row = []
        round_rocks, spaces = 0, 0
        for c in row:
            if c == '.':
                spaces += 1
            elif c == 'O':
                round_rocks += 1
            else:
                new_row += ['O' for _ in range(round_rocks)] + ['.' for _ in range(spaces)] + ['#']
                round_rocks, spaces = 0, 0
        new_row += ['O' for _ in range(round_rocks)] + ['.' for _ in range(spaces)]
        rows.append(new_row)
    return rows


def cycle(grid: [[chr]]) -> [[chr]]:
    grid = rot280(grid)
    for _ in range(4):
        grid = rot90(tilt_left(grid))
    return rot90(grid)


def part_one(data: str) -> int:
    grid = [[c for c in line] for line in data.splitlines()]
    grid = rot90(tilt_left(rot280(grid)))
    return sum(len(grid) - i for i, row in enumerate(grid) for c in row if c == 'O')


def part_two(data: str) -> int:
    grid = [[c for c in line] for line in data.splitlines()]
    visited = {}
    for k in range(1000):
        grid = cycle(grid)

        state = ''.join(c for row in grid for c in row)
        if state in visited and (1000000000 - k - 1) % (k - visited[state]) == 0:
            return sum(len(grid) - i for i, row in enumerate(grid) for c in row if c == 'O')
        else:
            visited[state] = k


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 14)
    print(part_one(input_data))
    print(part_two(input_data))
