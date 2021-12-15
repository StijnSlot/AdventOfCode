from util import aoc
import heapq


def neighbours(grid: list[list[int]], i: int, j: int) -> iter:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            yield x, y


def dijkstra(grid: list[list[int]]) -> int:
    queue = [(0, 0, 0)]
    distances = {}
    while len(queue) > 0:
        total, i, j = heapq.heappop(queue)
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            break
        for x, y in neighbours(grid, i, j):
            new_total = total + grid[x][y]
            if (x, y) not in distances or new_total < distances[(x, y)]:
                distances[(x, y)] = new_total
                heapq.heappush(queue, (new_total, x, y))
    return distances[(len(grid) - 1, len(grid[0]) - 1)]


def new_risk(small_grid: list[list[int]], i: int, j: int) -> int:
    add = i // len(small_grid) + j // len(small_grid[0])
    ans = add + small_grid[i % len(small_grid)][j % len(small_grid[0])]
    while ans >= 10:
        ans -= 9
    return ans


def part_one(data: str) -> int:
    grid = [[int(x) for x in row] for row in data.splitlines()]
    return dijkstra(grid)


def part_two(data: str) -> int:
    small_grid = [[int(x) for x in row] for row in data.splitlines()]
    grid = [[new_risk(small_grid, i, j) for j in range(5 * len(small_grid[0]))] for i in range(5 * len(small_grid))]
    return dijkstra(grid)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 15)
    print(part_one(input_data))
    print(part_two(input_data))
