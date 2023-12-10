from util import aoc
import re
from math import gcd
from functools import reduce


def parse_data(data: str) -> (str, {str, (str, str)}):
    part1, part2 = data.split('\n\n')
    nodes = {}
    for line in part2.splitlines():
        match = re.match("(\w+) = \((\w+), (\w+)", line)
        nodes[match.group(1)] = (match.group(2), match.group(3))
    print(part1, nodes)
    return part1, nodes


def count_steps(instructions, nodes, start, end_suffix):
    cur = start
    steps = 0
    while not cur.endswith(end_suffix):
        instr = instructions[steps % len(instructions)]
        cur = nodes[cur][0] if instr == 'L' else nodes[cur][1]
        steps += 1
    return steps


def lcm(a, b):
    return (int)((a * b) / gcd(a, b))


def part_one(data: str) -> int:
    instructions, nodes = parse_data(data)
    return count_steps(instructions, nodes, 'AAA', 'ZZZ')


def part_two(data: str) -> int:
    instructions, nodes = parse_data(data)
    cur_nodes = [x for x in nodes if x[-1] == 'A']
    goal_steps = [count_steps(instructions, nodes, x, 'Z') for x in cur_nodes]
    return reduce(lcm, goal_steps)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 8)
    print(part_one(input_data))
    print(part_two(input_data))
