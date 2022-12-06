from util import aoc
import re


def read_data(data: str) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    parts = data.split("\n\n")
    lines = parts[0].splitlines()
    nr_of_stacks = int(lines[-1].split()[-1])
    stacks = [[] for _ in range(nr_of_stacks)]
    for i in range(len(lines) - 1):
        for j in range(nr_of_stacks):
            if len(lines[i]) > j * 4 + 1 and lines[i][j * 4 + 1] != ' ':
                stacks[j].append(lines[i][j * 4 + 1])
    commands = []
    for line in parts[1].splitlines():
        match = re.match("move (\d+) from (\d+) to (\d+)", line)
        x, y, z = match.groups()
        commands.append((int(x), int(y) - 1, int(z) - 1))
    return stacks, commands


def perform_moves(stacks: list[list[str]], commands: list[tuple[int, int, int]], reverse: bool = False) -> list[list[str]]:
    for x, y, z in commands:
        stacks[z] = (stacks[y][:x][::-1] if reverse else stacks[y][:x]) + stacks[z]
        stacks[y] = stacks[y][x:]
    return stacks


def result(stacks: list[list[str]]) -> str:
    return "".join(x[0] if len(x) > 0 else ' ' for x in stacks)


def part_one(data: str) -> str:
    stacks, commands = read_data(data)
    perform_moves(stacks, commands, reverse=True)
    return result(stacks)


def part_two(data: str) -> str:
    stacks, commands = read_data(data)
    perform_moves(stacks, commands)
    return result(stacks)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 5)
    print(part_one(input_data))
    print(part_two(input_data))
