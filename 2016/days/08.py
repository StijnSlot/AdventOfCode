from util import aoc


_width = 50
_height = 6


def update_screen(line: str, grid: list[list[bool]]) -> None:
    commands = line.split()
    if commands[0] == "rect":
        x, y = commands[1].split('x')
        for i in range(int(y)):
            for j in range(int(x)):
                grid[i][j] = True
    else:
        if commands[1] == "column":
            x, k = int(commands[2][2:]), int(commands[4])
            old = [grid[i][x] for i in range(len(grid))]
            for i in range(len(grid)):
                grid[i][x] = old[(i - k) % len(grid)]
        else:
            y, k = int(commands[2][2:]), int(commands[4])
            old = [cell for cell in grid[y]]
            for i in range(len(grid[0])):
                grid[y][i] = old[(i - k) % len(grid[y])]


def part_one(data: str) -> int:
    grid = [[False for _ in range(_width)] for _ in range(_height)]
    for line in data.splitlines():
        update_screen(line, grid)
    return sum(1 for row in grid for x in row if x)


def part_two(data: str) -> str:
    grid = [[False for _ in range(_width)] for _ in range(_height)]
    for line in data.splitlines():
        update_screen(line, grid)
    return "\n".join("".join('#' if x else ' ' for x in row) for row in grid)


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 8)
    print(part_one(input_data))
    print(part_two(input_data))
