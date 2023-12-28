from util import aoc
import re
from dataclasses import dataclass, field
import random
from math import prod


@dataclass
class Node:
    name: str
    adj: [int] = field(default_factory=list)
    merge_count: int = 1


def parse_graph(data: str) -> [Node]:
    node_name_map, i = {}, 0
    nodes = []
    for line in data.splitlines():
        words = re.findall("(\w+)", line)
        for w in words:
            if w not in node_name_map:
                node_name_map[w] = i
                nodes.append(Node(w))
                i += 1
        u = node_name_map[words[0]]
        for w in words[1:]:
            v = node_name_map[w]
            nodes[u].adj.append(v)
            nodes[v].adj.append(u)
    return nodes


def karger(start_nodes: [Node]) -> int:
    while True:
        nodes = {i: Node(x.name, [a for a in x.adj]) for i, x in enumerate(start_nodes)} # copy
        while len(nodes) > 2:
            # pick random edge
            u = random.choice(list(nodes))
            v = random.choice(nodes[u].adj)

            # merge nodes
            for w in nodes[v].adj:
                nodes[w].adj.remove(v)
                if w != u:
                    nodes[w].adj.append(u)
                    nodes[u].adj.append(w)
            nodes[u].merge_count += nodes[v].merge_count
            del nodes[v]

        if sum(len(nodes[i].adj) for i in nodes) == 6:  # double counts edges
            return prod(nodes[i].merge_count for i in nodes)


def part_one(data: str) -> int:
    nodes = parse_graph(data)
    return karger(nodes)


def part_two(data: str) -> int:
    return None


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 25)
    print(part_one(input_data))
