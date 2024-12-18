from util import aoc
from collections import deque


MOVE_MAP = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
PART2_GRID_MAP = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}


def read_data(data: str) -> ([[chr]], [(int, int)], int, int):
    p1, p2 = data.split('\n\n')
    grid = [[c for c in line] for line in p1.splitlines()]
    moves = [MOVE_MAP[x] for x in ''.join(line for line in p2.splitlines())]
    start_i, start_j = next((i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == '@')
    return grid, moves, start_i, start_j


def push(grid: [[chr]], start_i: int, start_j: int, di: int, dj: int) -> bool:
    Q = deque()
    visited = []
    Q.append((start_i, start_j))
    while len(Q):
        i, j = Q.popleft()
        if (i, j) in visited:
            continue
        visited.append((i, j))
        next_i, next_j = i + di, j + dj
        if grid[next_i][next_j] == '#':
            return False
        elif grid[next_i][next_j] in ('O', '[', ']'):
            Q.append((next_i, next_j))
            if di != 0:
                if grid[next_i][next_j] == '[':
                    Q.append((next_i, next_j + 1))
                elif grid[next_i][next_j] == ']':
                    Q.append((next_i, next_j - 1))
    for i, j in visited[::-1]:
        grid[i + di][j + dj] = grid[i][j]
        grid[i][j] = '.'
    return True


def do_moves(grid: [[chr]], moves: [(int, int)], start_i: int, start_j: int):
    i, j = start_i, start_j
    for di, dj in moves:
        pushed = push(grid, i, j, di, dj)
        if pushed:
            i += di
            j += dj


def score(grid: [[chr]]) -> int:
    return sum(100 * i + j for i, row in enumerate(grid) for j, x in enumerate(row) if x in ('[', 'O'))


def part_one(data: str) -> int:
    grid, moves, start_i, start_j = read_data(data)
    do_moves(grid, moves, start_i, start_j)
    return score(grid)


def part_two(data: str) -> int:
    grid, moves, start_i, start_j = read_data(data)
    grid = [[x for x in ''.join(PART2_GRID_MAP[c] for c in row)] for row in grid]
    do_moves(grid, moves, start_i, 2 * start_j)
    return score(grid)


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 15)
    print(part_one(input_data))
    print(part_two(input_data))
