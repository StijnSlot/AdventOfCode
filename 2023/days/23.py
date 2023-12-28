from util import aoc
from dataclasses import dataclass, field
from enum import Enum
from collections import deque


class Dir(Enum):
    U = (0, -1)
    D = (0, 1)
    L = (-1, 0)
    R = (1, 0)


@dataclass
class Region:
    cells: {(int, int)}
    adj: [int] = field(default_factory=list)


def longest_path(grid, regions, start_region, end_region):
    max_ans = 0
    stack = [(start_region, [start_region])]
    visited = set()
    while stack:
        r, path = stack.pop()
        key = ','.join((str(x) for x in sorted(path))) + ':' + str(r)
        if key in visited:
            continue
        visited.add(key)
        if r == end_region:
            # for i in range(len(grid)):
            #     for j in range(len(grid[0])):
            #         if any((j, i) in regions[u].cells for u in visited_regions):
            #             print('O', end='')
            #         else:
            #             print(grid[i][j], end='')
            #     print()
            ans = sum(len(regions[u].cells) for u in path) + len(path) - 2
            # print(ans, max_ans, len(path), path)
            max_ans = max(max_ans, ans)
        for u in regions[r].adj:
            if u not in path:
                stack.append((u, path + [u]))
    return max_ans


def flood_fill(grid, start_x, start_y):
    cells = set()
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        cells.add((x, y))
        for dir in Dir:
            new_x, new_y = x + dir.value[0], y + dir.value[1]
            if 0 <= new_x < len(grid[0]) \
                    and 0 <= new_y < len(grid) \
                    and grid[new_y][new_x] == '.' \
                    and (new_x, new_y) not in cells:
                queue.append((new_x, new_y))
    return cells


def part_one(data: str) -> int:
    grid = [list(line) for line in data.splitlines()]
    region_map = {}
    regions = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '.' and (x, y) not in region_map:
                cells = flood_fill(grid, x, y)
                regions.append(Region(cells))
                region_map.update({(xx, yy): len(regions) - 1 for xx, yy in cells})
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '>':
                regions[region_map[(x-1, y)]].adj.append(region_map[(x+1, y)])
            elif c == '<':
                regions[region_map[(x+1, y)]].adj.append(region_map[(x-1, y)])
            elif c == 'v':
                regions[region_map[(x, y-1)]].adj.append(region_map[(x, y+1)])
            elif c == '^':
                regions[region_map[(x, y+1)]].adj.append(region_map[(x, y-1)])
    start_region = region_map[(1, 0)]
    end_region = region_map[(len(grid[0]) - 2, len(grid) - 1)]
    return longest_path(grid, regions, start_region, end_region)


def part_two(data: str) -> int:
    grid = [list(line) for line in data.splitlines()]
    region_map = {}
    regions = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '.' and (x, y) not in region_map:
                cells = flood_fill(grid, x, y)
                regions.append(Region(cells))
                region_map.update({(xx, yy): len(regions) - 1 for xx, yy in cells})
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '>':
                regions[region_map[(x - 1, y)]].adj.append(region_map[(x + 1, y)])
                regions[region_map[(x + 1, y)]].adj.append(region_map[(x - 1, y)])
            elif c == '<':
                regions[region_map[(x - 1, y)]].adj.append(region_map[(x + 1, y)])
                regions[region_map[(x + 1, y)]].adj.append(region_map[(x - 1, y)])
            elif c == 'v':
                regions[region_map[(x, y - 1)]].adj.append(region_map[(x, y + 1)])
                regions[region_map[(x, y + 1)]].adj.append(region_map[(x, y - 1)])
            elif c == '^':
                regions[region_map[(x, y - 1)]].adj.append(region_map[(x, y + 1)])
                regions[region_map[(x, y + 1)]].adj.append(region_map[(x, y - 1)])
    start_region = region_map[(1, 0)]
    end_region = region_map[(len(grid[0]) - 2, len(grid) - 1)]
    return longest_path(grid, regions, start_region, end_region)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 23)
    print(part_one(input_data))
    print(part_two(input_data))
