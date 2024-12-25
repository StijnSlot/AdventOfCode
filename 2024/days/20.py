from util import aoc
from collections import deque


DD = ((0, 1), (1, 0), (0, -1), (-1, 0))


def read_data(data: str) -> ([[chr]], (int, int), (int, int)):
    grid = [[c for c in line] for line in data.splitlines()]
    start = next((i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 'S')
    end = next((i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 'E')
    return grid, start, end


def bfs(grid: [[chr]],
        start_i: int,
        start_j: int,
        max_dis: int = 9999999,
        ignore_obs: bool = False) -> {(int, int), int}:
    Q = deque()
    Q.append((0, start_i, start_j))
    dis = {}
    while len(Q) > 0:
        d, i, j = Q.popleft()
        if (i, j) in dis or d > max_dis:
            continue
        dis[(i, j)] = d
        for di, dj in DD:
            new_i, new_j = i + di, j + dj
            if ignore_obs or grid[new_i][new_j] != '#':
                Q.append((d + 1, new_i, new_j))
    return dis


def sum_cheat_dis2(grid: [[chr]], dis_e: {(int, int), int}, start_i: int, start_j: int, steps: int, max_dis: int) -> int:
    dis = bfs(grid, start_i, start_j, max_dis=steps, ignore_obs=True)
    return sum(1 for i, j in dis if (i, j) in dis_e if dis[(i, j)] + dis_e[(i, j)] <= max_dis)


def part_one(data: str) -> int:
    grid, start, end = read_data(data)
    dis_s = bfs(grid, *start)
    dis_e = bfs(grid, *end)
    original_dis = dis_s[end]
    return sum(sum_cheat_dis2(grid, dis_e, i, j, 2, original_dis - d - 100)
               for (i, j), d in dis_s.items())


def part_two(data: str) -> int:
    grid, start, end = read_data(data)
    dis_s = bfs(grid, *start)
    dis_e = bfs(grid, *end)
    original_dis = dis_s[end]
    return sum(sum_cheat_dis2(grid, dis_e, i, j, 20, original_dis - d - 100)
               for (i, j), d in dis_s.items())


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 20)
    print(part_one(input_data))
    print(part_two(input_data))
