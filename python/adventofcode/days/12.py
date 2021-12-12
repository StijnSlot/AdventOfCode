from adventofcode.util import aoc


class Node:
    def __init__(self, key: str):
        self.key = key
        self.large = key.isupper()
        self.adj = set()
        self.visited = 0


def get_nodes(data: str) -> dict[str, Node]:
    nodes = {}
    for row in data.splitlines():
        x, y = row.split('-')
        if x not in nodes:
            nodes[x] = Node(x)
        if y not in nodes:
            nodes[y] = Node(y)
        nodes[x].adj.add(y)
        nodes[y].adj.add(x)
    return nodes


def paths(nodes: dict[str, Node], v: Node, visited_twice: bool) -> int:
    if v.key == 'end':
        return 1
    v.visited += 1
    num_paths = 0
    for x in v.adj:
        u = nodes[x]
        if u.visited == 0 or u.large:
            num_paths += paths(nodes, u, visited_twice)
        elif not visited_twice and u.visited == 1 and x != 'start':
            num_paths += paths(nodes, u, True)
    v.visited -= 1
    return num_paths


def part_one(data: str) -> int:
    nodes = get_nodes(data)
    return paths(nodes, nodes['start'], True)


def part_two(data: str) -> int:
    nodes = get_nodes(data)
    return paths(nodes, nodes['start'], False)


if __name__ == "__main__":
    input_data = aoc.get_input(12)
    print(part_one(input_data))
    print(part_two(input_data))
