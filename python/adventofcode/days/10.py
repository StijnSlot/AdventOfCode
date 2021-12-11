from typing import Optional
from adventofcode.util import aoc

bracket_map = {'(': ')', '[': ']', '{': '}', '<': '>'}


def find_corrupted(line: str, i: int, open_brackets: list[str]) -> Optional[str]:
    if i >= len(line):
        return None
    if line[i] in bracket_map:
        open_brackets.append(line[i])
        return find_corrupted(line, i+1, open_brackets)
    last = open_brackets.pop() if len(open_brackets) > 0 else None
    if line[i] == bracket_map[last]:
        return find_corrupted(line, i + 1, open_brackets)
    return line[i]


def part_one(data: str) -> int:
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
    return sum(score_map[find_corrupted(line, 0, [])] for line in data.splitlines())


def part_two(data: str) -> int:
    score_map = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in data.splitlines():
        open_br = []
        if find_corrupted(line, 0, open_br) is None:
            scores.append(sum(5 ** i * score_map[bracket_map[open_br[i]]] for i in reversed(range(len(open_br)))))
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    input_data = aoc.get_input(10)
    print(part_one(input_data))
    print(part_two(input_data))
