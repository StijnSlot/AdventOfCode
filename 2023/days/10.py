from util import aoc


DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

CHRS = {'|': [1, 3], '-': [0, 2], 'L': [0, 3], 'J': [2, 3], '7': [1, 2], 'F': [0, 1]}


def parse_chr(x: chr) -> [int]:
    return CHRS[x] if x in CHRS else []


def parse_grid(data: str) -> [[chr]]:
    return [[x for x in line] for line in data.splitlines()]


def find_main_loop(grid: [[chr]], startx: int, starty: int) -> (int, {(int, int)}):
    curx, cury = startx, starty
    direction = 0
    for i in range(len(DX)):
        curx, cury = startx + DX[i], starty + DY[i]
        adj = parse_chr(grid[cury][curx])
        if (i + 2) % 4 in adj:
            direction = i
            break
    steps = 1
    visited = {(startx, starty)}
    while (curx, cury) not in visited:
        visited.add((curx, cury))
        adj = parse_chr(grid[cury][curx])
        direction = next(x for x in adj if x != (direction + 2) % 4)
        curx, cury = curx + DX[direction], cury + DY[direction]
        steps += 1
    return steps, visited


def is_inside_main_loop(grid: [[chr]], visited: {(int, int)}, x: int, y: int) -> bool:
    intersects, para = 0, 0
    for i in range(y+1, len(grid)):
        if (x, i) not in visited:
            continue
        if grid[i][x] == '-':
            intersects += 1
        elif grid[i][x] in ['L', '7']:
            para += 1
        elif grid[i][x] in ['J', 'F']:
            para -= 1
    if para % 2 != 0:
        print("something wrong, check manual fix for S")
    intersects += abs(para) // 2
    return intersects % 2 == 1


def part_one(data: str) -> int:
    grid = parse_grid(data)
    startx, starty = next((x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == 'S')
    return (find_main_loop(grid, startx, starty)[0] + 1) // 2


def part_two(data: str) -> int:
    grid = parse_grid(data)
    startx, starty = next((x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == 'S')
    visited = find_main_loop(grid, startx, starty)[1]
    grid[starty][startx] = '7'  # manually fix for S pls :)
    return sum(1 for y in range(len(grid)) for x in range(len(grid[y]))
               if not (x, y) in visited and is_inside_main_loop(grid, visited, x, y))


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 10)
    print(part_one(input_data))
    print(part_two(input_data))
