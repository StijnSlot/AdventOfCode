from util import aoc
from queue import PriorityQueue
from collections import deque
from dataclasses import dataclass


DD = ((0, 1), (1, 0), (0, -1), (-1, 0))


@dataclass(frozen=True, order=True)
class SearchState:
    i: int
    j: int
    direction: int


def dijkstra(grid: [[str]], start_i: int, start_j: int) -> ({SearchState, int}, {SearchState, set[SearchState]}):
    costs, best_dir = {}, {}
    Q = PriorityQueue()
    Q.put((0, SearchState(start_i, start_j, 0), SearchState(start_i, start_j, 0)))
    while Q.qsize() > 0:
        c, ss, last_ss = Q.get()
        if ss in costs and costs[ss] <= c:
            if costs[ss] == c:
                best_dir[ss].add(last_ss)
            continue
        best_dir[ss] = {last_ss}
        costs[ss] = c

        Q.put((c + 1000, SearchState(ss.i, ss.j, (ss.direction + 1) % 4), ss))
        Q.put((c + 1000, SearchState(ss.i, ss.j, (ss.direction - 1) % 4), ss))
        di, dj = DD[ss.direction]
        new_i, new_j = ss.i + di, ss.j + dj
        if grid[new_i][new_j] == '.':
            Q.put((c + 1, SearchState(new_i, new_j, ss.direction), ss))
    return costs, best_dir


def bfs(best_dir: {SearchState, set[SearchState]}, start_ss: SearchState) -> {(int, int)}:
    visited = set()
    Q = deque()
    Q.append(start_ss)
    while len(Q) > 0:
        ss = Q.popleft()
        if ss in visited:
            continue
        visited.add(ss)
        for new_ss in best_dir[ss]:
            Q.append(new_ss)
    return {(ss.i, ss.j) for ss in visited}


def part_one(data: str) -> int:
    grid = [[c for c in row] for row in data.splitlines()]
    start_i, start_j = next((i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 'S')
    end_i, end_j = next((i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 'E')
    grid[start_i][start_j] = '.'
    grid[end_i][end_j] = '.'
    costs, _ = dijkstra(grid, start_i, start_j)
    return min(costs[SearchState(end_i, end_j, k)] for k in range(len(DD)))


def part_two(data: str) -> int:
    grid = [[c for c in row] for row in data.splitlines()]
    start_i, start_j = next((i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 'S')
    end_i, end_j = next((i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 'E')
    grid[start_i][start_j] = '.'
    grid[end_i][end_j] = '.'
    costs, best_dir = dijkstra(grid, start_i, start_j)
    _, k = min((costs[SearchState(end_i, end_j, k)], k) for k in range(len(DD)))
    return len(bfs(best_dir, SearchState(end_i, end_j, k)))


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 16)
    print(part_one(input_data))
    print(part_two(input_data))
