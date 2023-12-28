from util import aoc
from enum import Enum
from queue import PriorityQueue
from functools import total_ordering


@total_ordering
class Dir(Enum):
    N = (0, -1)
    S = (0, 1)
    W = (-1, 0)
    E = (1, 0)

    def __lt__(self, other):
        if self == other:
            return False
        for dir in Dir:
            if dir == self:
                return True
            if dir == other:
                return False


rev_order = {Dir.N: Dir.S, Dir.S: Dir.N, Dir.W: Dir.E, Dir.E: Dir.W}


def heat_loss_path(grid, min_step, max_step):
    visited = {}
    goal_x, goal_y = len(grid[0]) - 1, len(grid) - 1
    queue = PriorityQueue()
    queue.put((0, 0, 0, None))
    while queue:
        dis, x, y, prev_dir = queue.get()
        if (x, y, prev_dir) in visited and visited[(x, y, prev_dir)] <= dis:
            continue
        visited[(x, y, prev_dir)] = dis
        if x == goal_x and y == goal_y:
            return dis
        for dir in Dir:
            if prev_dir == dir or rev_order[dir] == prev_dir:
                # cannot go same dir or in reverse
                continue
            for k in range(min_step, max_step + 1):
                new_x, new_y = x + k * dir.value[0], y + k * dir.value[1]
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                    new_dis = dis + sum(grid[y + i * dir.value[1]][x + i * dir.value[0]] for i in range(1, k + 1))
                    if (new_x, new_y, dir) not in visited or visited[(new_x, new_y, dir)] > new_dis:
                        queue.put((new_dis, new_x, new_y, dir))


def part_one(data: str) -> int:
    grid = [[int(x) for x in line] for line in data.splitlines()]
    return heat_loss_path(grid, 1, 3)


def part_two(data: str) -> int:
    grid = [[int(x) for x in line] for line in data.splitlines()]
    return heat_loss_path(grid, 4, 10)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 17)
    print(part_one(input_data))
    print(part_two(input_data))
