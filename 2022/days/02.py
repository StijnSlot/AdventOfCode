from util import aoc


def part_one(data: str) -> int:
    score = 0
    extra = {'X': 1, 'Y': 2, 'Z': 3}
    draws = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    beats = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    for line in data.splitlines():
        first, second = line.split()
        score += extra[second]
        if draws[first] == second:
            score += 3
        elif beats[first] == second:
            score += 6
    return score


def part_two(data: str) -> int:
    score = 0
    extra = {'A': 1, 'B': 2, 'C': 3}
    beats = {'A': 'B', 'B': 'C', 'C': 'A'}
    for line in data.splitlines():
        first, second = line.split()
        if second == 'X':
            score += extra[beats[beats[first]]]
        elif second == 'Y':
            score += extra[first] + 3
        else:
            score += extra[beats[first]] + 6
    return score


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 2)
    print(part_one(input_data))
    print(part_two(input_data))
