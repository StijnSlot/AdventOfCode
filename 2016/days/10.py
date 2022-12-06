from dataclasses import dataclass
from util import aoc
import re
from typing import Generator


_rule_str = "bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
_input_str = "value (\d+) goes to bot (\d+)"
goal_x = "17"
goal_y = "61"
_output = "output"


@dataclass
class Node:
    """Class for keeping track of a bots rule and its items"""
    rule: tuple[str, str]
    items: list[str]


def simulate(nodes: dict[str, Node], a: str) -> Generator[str, None, None]:
    if a == _output or len(nodes[a].items) < 2:
        return
    x, y = sorted(nodes[a].items)
    if x == goal_x and y == goal_y:
        yield a
    b, c = nodes[a].rule
    nodes[b].items.append(x)
    nodes[c].items.append(y)
    yield from simulate(nodes, b)
    yield from simulate(nodes, c)
    nodes[a].items = []


def part_one(data: str) -> str:
    nodes = {_output: Node(rule=("", ""), items=[])}
    lines = data.splitlines()
    for line in lines:
        match = re.match(_rule_str, line)
        if match is None:
            continue
        a, x, b, y, c = (x for x in match.groups())
        u, v = (x if x == _output else b), (y if y == _output else c)
        nodes[a] = Node(rule=(u, v), items=[])
    print(nodes)
    for line in lines:
        match = re.match(_input_str, line)
        if match is None:
            continue
        a, b = match.groups()
        nodes[b].items.append(a)
        result = next(simulate(nodes, b), None)
        if result is not None:
            return result


def part_two(data: str) -> int:
    return None


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 10)
    print(part_one(input_data))
    print(part_two(input_data))
