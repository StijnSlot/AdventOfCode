from util import aoc
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Node:
    name: str
    adj: [str]

    def __hash__(self): return hash(self.name)


def read_nodes(data: str) -> {str, Node}:
    nodes = {}
    for line in data.splitlines():
        a, b = line.split('-')
        if a not in nodes:
            nodes[a] = Node(a, [b])
        else:
            nodes[a].adj.append(b)
        if b not in nodes:
            nodes[b] = Node(b, [a])
        else:
            nodes[b].adj.append(a)
    return nodes


def three_sets(nodes: {str, Node}, v: str) -> [tuple[str, str, str]]:
    return [tuple(sorted((v, a, b)))
            for a, b in combinations(nodes[v].adj, 2)
            if a in nodes[b].adj and b in nodes[a].adj]


def bronKerbosch(nodes: {str, Node}, R: {str}, P: {str}, X: {str}) -> {str}:
    if len(P) == 0 and len(X) == 0:
        return {','.join(sorted(R))}
    cliques = set()
    for v in P:
        cliques = cliques | bronKerbosch(nodes, R | {v}, P & set(nodes[v].adj), X & set(nodes[v].adj))
        P = P - {v}
        X = X | {v}
    return cliques


def part_one(data: str) -> int:
    nodes = read_nodes(data)
    return len({x for v in nodes for x in three_sets(nodes, v) if v[0] == 't'})


def part_two(data: str) -> str:
    nodes = read_nodes(data)
    cliques = bronKerbosch(nodes, set(), set(nodes.keys()), set())
    return max(cliques, key=lambda c: len(c.split(',')))


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 23)
    print(part_one(input_data))
    print(part_two(input_data))
