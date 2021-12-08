from adventofcode.util import aoc


def read_lines(data: str) -> list[str]:
    lines = []
    for row in data.splitlines():
        start, end = row.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        lines.append((int(x1), int(y1), int(x2), int(y2)))
    return lines


def create_grid(lines: list[str], allow_diagonal: bool) -> list[list[int]]:
    grid_size = max(max(line) for line in lines) + 1
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for line in lines:
        if line[0] == line[2]:
            for k in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                grid[line[0]][k] += 1
        elif line[1] == line[3]:
            for k in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                grid[k][line[1]] += 1
        elif allow_diagonal:
            dx, dy = line[2] - line[0], line[3] - line[1]
            delta, dx, dy = abs(dx), int(dx / abs(dx)), int(dy / abs(dy))
            for k in range(delta + 1):
                grid[line[0] + k * dx][line[1] + k * dy] += 1
    return grid


def part_one(data: str) -> int:
    lines = read_lines(data)
    grid = create_grid(lines, False)
    return sum(1 for row in grid for x in row if x >= 2)


def part_two(data: str) -> int:
    lines = read_lines(data)
    grid = create_grid(lines, True)
    return sum(1 for row in grid for x in row if x >= 2)


if __name__ == "__main__":
    input_data = aoc.get_input(5)
    print(part_one(input_data))
    print(part_two(input_data))
