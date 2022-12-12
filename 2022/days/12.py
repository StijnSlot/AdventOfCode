from util import aoc
from collections import deque


_dif = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> int:
    queue = deque([(0, start)])
    visited = set()
    while len(queue) > 0:
        dis, u = queue.popleft()
        if u == end:
            return dis
        if u in visited:
            continue
        visited.add(u)
        elev_u = grid[u[0]][u[1]]
        for dx, dy in _dif:
            v = (u[0] + dx, u[1] + dy)
            if v in visited:
                continue
            if not (0 <= v[0] < len(grid) and 0 <= v[1] < len(grid[0])):
                continue
            elev_v = grid[v[0]][v[1]]
            if elev_v - elev_u <= 1:
                queue.append((dis + 1, v))
    return 99999999


def find_char_in_grid(grid: list[list], c: str) -> tuple[int, int]:
    return next((i, j) for i, line in enumerate(grid) for j, _ in enumerate(line) if grid[i][j] == c)


def parse_data(data: str) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    grid = [[(ord(x) - ord('a') if x not in ['S', 'E'] else x) for x in line] for line in data.splitlines()]
    start = find_char_in_grid(grid, 'S')
    end = find_char_in_grid(grid, 'E')
    grid[start[0]][start[1]] = 0
    grid[end[0]][end[1]] = 25
    return grid, start, end


def part_one(data: str) -> int:
    grid, start, end = parse_data(data)
    return bfs(grid, start, end)


def part_two(data: str) -> int:
    grid, _, end = parse_data(data)
    return min(bfs(grid, (i, j), end) for i, line in enumerate(grid) for j, _ in enumerate(line) if grid[i][j] == 0)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 12)
    print(part_one(input_data))
    print(part_two(input_data))
