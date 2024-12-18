from util import aoc
from collections import deque


DD = ((0, 1), (1, 0), (0, -1), (-1, 0))
GRID_SIZE = 70


def bfs(start_x: int, start_y: int, falling_bytes: [int]) -> int:
    Q = deque()
    Q.append((0, start_x, start_y))
    visited = set(falling_bytes)
    while len(Q) > 0:
        steps, x, y = Q.popleft()
        if x == GRID_SIZE and y == GRID_SIZE:
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in DD:
            x2, y2 = x + dx, y + dy
            if 0 <= x2 <= GRID_SIZE and 0 <= y2 <= GRID_SIZE and (x2, y2) not in visited:
                Q.append((steps + 1, x2, y2))
    return -1


def part_one(data: str) -> int:
    falling_bytes = [tuple(int(x) for x in line.split(',')) for line in data.splitlines()]
    return bfs(0, 0, falling_bytes[:1024])


def part_two(data: str) -> (int, int):
    falling_bytes = [tuple(int(x) for x in line.split(',')) for line in data.splitlines()]
    return next(falling_bytes[i-1] for i in range(len(falling_bytes)) if bfs(0, 0, falling_bytes[:i]) == -1)


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 18)
    print(part_one(input_data))
    print(part_two(input_data))
