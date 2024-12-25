from util import aoc
from functools import lru_cache
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def add(self, p):
        return Point(self.x + p.x, self.y + p.y)


NUMERICAL_KEYPAD = {'0': Point(1, 0), 'A': Point(2, 0), '1': Point(0, 1), '2': Point(1, 1),
                    '3': Point(2, 1), '4': Point(0, 2), '5': Point(1, 2), '6': Point(2, 2),
                    '7': Point(0, 3), '8': Point(1, 3), '9': Point(2, 3)}
DIRECTIONAL_KEYPAD = {'<': Point(0, 0), 'v': Point(1, 0), '>': Point(2, 0), '^': Point(1, 1), 'A': Point(2, 1)}
DD = {'>': Point(1, 0), 'v': Point(0, -1), '<': Point(-1, 0), '^': Point(0, 1)}


def path_seq(cur: Point, goal: Point) -> (str, str):
    x = ('>' if cur.x < goal.x else '<') * abs(goal.x - cur.x)
    y = ('^' if cur.y < goal.y else 'v') * abs(goal.y - cur.y)
    return x + y, y + x  # only consider L shaped paths


def hits_gap(cur: Point, s: str, numerical: bool) -> bool:
    p = cur
    for c in s:
        p = p.add(DD[c])
        if numerical and p == Point(0, 0):
            return True
        if not numerical and p == Point(0, 1):
            return True
    return False


@lru_cache(maxsize=None)
def numerical_seqs(cur_c: chr, goal_c: chr) -> {str}:
    cur = NUMERICAL_KEYPAD[cur_c]
    goal = NUMERICAL_KEYPAD[goal_c]
    return {ss + 'A' for ss in path_seq(cur, goal) if not hits_gap(cur, ss, True)}


@lru_cache(maxsize=None)
def directional_seqs(cur_c: chr, goal_c: chr) -> {str}:
    cur = DIRECTIONAL_KEYPAD[cur_c]
    goal = DIRECTIONAL_KEYPAD[goal_c]
    return {ss + 'A' for ss in path_seq(cur, goal) if not hits_gap(cur, ss, False)}


@lru_cache(maxsize=None)
def shortest_seq(code: str, nr_robots: int, start: bool) -> int:
    if nr_robots == 0:
        return len(code)
    answer, prev = 0, 'A'
    for i, c in enumerate(code):
        seqs = numerical_seqs(prev, c) if start else directional_seqs(prev, c)
        answer += min(shortest_seq(x, nr_robots - 1, False) for x in seqs)
        prev = c
    return answer


def part_one(data: str) -> int:
    return sum(int(line[:-1]) * shortest_seq(line, 3, True) for line in data.splitlines())


def part_two(data: str) -> int:
    return sum(int(line[:-1]) * shortest_seq(line, 26, True) for line in data.splitlines())


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 21)
    print(part_one(input_data))
    print(part_two(input_data))
