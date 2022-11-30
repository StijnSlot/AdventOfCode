from util import aoc


def most_common_char(line: str) -> str:
    return sorted((line.count(c), c) for c in set(line))[-1][1]


def least_common_char(line: str) -> str:
    return sorted((line.count(c), c) for c in set(line))[0][1]


def part_one(data: str) -> str:
    grid = [[c for c in line] for line in data.splitlines()]
    rot_grid = ["".join(grid[j][i] for j in range(len(grid))) for i in range(len(grid[0]))]
    return "".join(most_common_char(line) for line in rot_grid)


def part_two(data: str) -> str:
    grid = [[c for c in line] for line in data.splitlines()]
    rot_grid = ["".join(grid[j][i] for j in range(len(grid))) for i in range(len(grid[0]))]
    return "".join(least_common_char(line) for line in rot_grid)


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 6)
    print(part_one(input_data))
    print(part_two(input_data))
