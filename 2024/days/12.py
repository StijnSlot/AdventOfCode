from util import aoc
from collections import deque


DD = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(grid, start_i, start_j):
    plot = grid[start_i][start_j]
    Q, visited, perimeter = deque(), {(start_i, start_j)}, {}
    Q.append((start_i, start_j))
    while len(Q) > 0:
        i, j = Q.popleft()
        for k, (di, dj) in enumerate(DD):
            new_i, new_j = i + di, j + dj
            if (new_i, new_j) in visited:
                continue
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == plot:
                visited.add((new_i, new_j))
                Q.append((new_i, new_j))
            else:
                if k not in perimeter:
                    perimeter[k] = []
                perimeter[k].append((new_i, new_j))
    return visited, perimeter


def nr_of_sides(perimeter):
    nr_edges = 0
    for k, edges in perimeter.items():
        # reverse depending on direction of perimeter, to sort in right order
        edges = sorted(((i, j) if k % 2 == 1 else (j, i) for (i, j) in edges))

        nr_edges += 1
        for i in range(len(edges) - 1):
            x1, y1 = edges[i]
            x2, y2 = edges[i + 1]
            if x1 != x2 or y2 - y1 > 1:
                nr_edges += 1
    return nr_edges


def price(grid, part2=False):
    total_visited, total = set(), 0
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if (i, j) not in total_visited:
                visited, perimeter = bfs(grid, i, j)
                total_visited = total_visited.union(visited)
                total += len(visited) * (nr_of_sides(perimeter) if part2 else sum(len(z) for z in perimeter.values()))
    return total


def part_one(data: str) -> int:
    grid = [[c for c in line] for line in data.splitlines()]
    return price(grid)


def part_two(data: str) -> int:
    grid = [[c for c in line] for line in data.splitlines()]
    return price(grid, part2=True)


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 12)
    print(part_one(input_data))
    print(part_two(input_data))
