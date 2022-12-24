from util import aoc
from queue import PriorityQueue
from functools import lru_cache


_winds_vert = {}
_winds_hor = {}
_height = 0
_width = 0


@lru_cache(maxsize=None)
def is_allowed(cur: tuple[int, int], k: int) -> bool:
    for i, di in _winds_vert[cur[1]]:
        wi = (i + di * k - 1) % (_height - 2) + 1
        if cur[0] == wi:
            return False
    for j, dj in _winds_hor[cur[0]]:
        wj = (j + dj * k - 1) % (_width - 2) + 1
        if cur[1] == wj:
            return False
    return True


def man_dis(x: tuple[int, int], y: [int, int]) -> int:
    return abs(y[0] - x[0]) + abs(y[1] - x[1])


def a_star(start: tuple[int, int], end: tuple[int, int], starti: int = 0) -> int:
    dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    Q = PriorityQueue()
    Q.put((starti + man_dis(start, end), starti, start))
    visited = set()
    while not Q.empty():
        d, i, cur = Q.get()
        if (i, cur) in visited:
            continue
        if cur == end:
            return i
        visited.add((i, cur))
        for di, dj in dd:
            v = (cur[0] + di, cur[1] + dj)
            if not (1 <= v[0] <= _height - 2 and 1 <= v[1] <= _width - 2 or v == end):
                continue
            if is_allowed(v, i + 1):
                Q.put((i + man_dis(v, end) + 1, i + 1, v))
        if is_allowed(cur, i + 1):
            Q.put((d + 1, i + 1, cur))
    raise ValueError("Impossible maze")


def read_grid(data: str) -> tuple[tuple[int, int], tuple[int, int]]:
    global _winds_vert, _winds_hor, _height, _width
    lines = data.splitlines()
    _height, _width = len(lines), len(lines[0])
    start = (0, next(i for i, x in enumerate(lines[0]) if x == '.'))
    _winds_vert = {i: [] for i in range(_width + 1)}
    _winds_hor = {i: [] for i in range(_height + 1)}
    end = (len(lines) - 1, next(i for i, x in enumerate(lines[-1]) if x == '.'))
    dwind = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x in dwind:
                di, dj = dwind[x]
                if di != 0:
                    _winds_vert[j].append((i, di))
                else:
                    _winds_hor[i].append((j, dj))
    return start, end


def part_one(data: str) -> int:
    start, end = read_grid(data)
    return a_star(start, end)


def part_two(data: str) -> int:
    start, end = read_grid(data)
    i = a_star(start, end)
    i = a_star(end, start, starti=i)
    return a_star(start, end, starti=i)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 24)
    print(part_one(input_data))
    print(part_two(input_data))
