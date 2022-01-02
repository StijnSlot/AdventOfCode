from copy import deepcopy


def part_one(data: str) -> int:
    grid = [[c for c in row] for row in data.splitlines()]
    moved = True
    steps = 0
    while moved:
        moved = False
        new_grid = deepcopy(grid)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '.' and grid[i][(j - 1) % len(row)] == '>':
                    new_grid[i][j] = '>'
                    new_grid[i][(j - 1) % len(row)] = '.'
                    moved = True
        grid = new_grid
        new_grid = deepcopy(grid)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '.' and grid[(i - 1) % len(grid)][j] == 'v':
                    new_grid[i][j] = 'v'
                    new_grid[(i - 1) % len(grid)][j] = '.'
                    moved = True
        steps += 1
        grid = new_grid
        print(steps)
        for row in grid:
            print("".join(row))
    return steps



def part_two(data: str) -> int:
    return None


if __name__ == "__main__":
    with open('../data/25.txt') as f:
        input_data = f.read()
    print(part_one(input_data))
    print(part_two(input_data))
