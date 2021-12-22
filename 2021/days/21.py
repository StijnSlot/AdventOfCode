from functools import cache
from util import aoc


def read_pos(data: str) -> (int, int):
    line1, line2 = data.splitlines()
    pos1 = int(line1.split()[-1])
    pos2 = int(line2.split()[-1])
    return pos1, pos2


def get_new_pos(pos: int, x: int, steps: int = 1) -> int:
    for k in range(steps):
        pos = (pos + x + k - 1) % 10 + 1
    return pos


def simulate(pos1: int, pos2: int, score1: int, score2: int, die: int, is_turn1: bool) -> (int, int, int):
    if score1 >= 1000 or score2 >= 1000:
        return score1, score2, die
    if is_turn1:
        new_pos1 = get_new_pos(pos1, die, 3)
        return simulate(new_pos1, pos2, score1 + new_pos1, score2, die + 3, False)
    else:
        new_pos2 = get_new_pos(pos2, die, 3)
        return simulate(pos1, new_pos2, score1, score2 + new_pos2, die + 3, True)


@cache
def get_paths(pos1: int, pos2: int, score1: int, score2: int, turn: int) -> (int, int):
    if score1 >= 21:
        return 1, 0
    elif score2 >= 21:
        return 0, 1
    paths = (0, 0)
    for die in range(1, 4):
        if turn < 3:
            new_pos1 = get_new_pos(pos1, die)
            new_score1 = score1 + new_pos1 if turn == 2 else score1
            new_paths = get_paths(new_pos1, pos2, new_score1, score2, (turn + 1) % 6)
        else:
            new_pos2 = get_new_pos(pos2, die)
            new_score2 = score2 + new_pos2 if turn == 5 else score2
            new_paths = get_paths(pos1, new_pos2, score1, new_score2, (turn + 1) % 6)
        paths = (paths[0] + new_paths[0], paths[1] + new_paths[1])
    return paths


def part_one(data: str) -> int:
    pos1, pos2 = read_pos(data)
    score1, score2, die = simulate(pos1, pos2, 0, 0, 1, True)
    return min(score1, score2) * (die - 1)


def part_two(data: str) -> int:
    pos1, pos2 = read_pos(data)
    return max(get_paths(pos1, pos2, 0, 0, 0))


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 21)
    print(part_one(input_data))
    print(part_two(input_data))
