from util import aoc


def swap_smudge(row: str, i: int) -> str:
    return row[:i] + ('.' if row[i] == '#' else '#') + (row[i+1:] if i < len(row) else '')


def has_reflection(row: str, i: int) -> int:
    reflection_length = min(i, len(row) - i)
    left, right = row[i-reflection_length:i], row[i:i+reflection_length]
    return left == right[::-1]


def hor_score(pattern: [str], col_to_skip: int = None) -> int:
    for i in range(1, len(pattern[0])):
        if i == col_to_skip:
            continue
        if all(has_reflection(row, i) for row in pattern):
            print('hor', i)
            return i
    return 0


def vert_score(pattern: [str], row_to_skip: int = None) -> int:
    for i in range(1, len(pattern)):
        if i == row_to_skip:
            continue
        if all(has_reflection(''.join(pattern[k][j] for k in range(len(pattern))), i) for j in range(len(pattern[0]))):
            print('vert', i)
            return i
    return 0


def score(pattern: [str], row_to_skip: int = None, col_to_skip: int = None) -> int:
    return 100 * vert_score(pattern, row_to_skip) + hor_score(pattern, col_to_skip)


def fix_smudge_and_score(pattern: [str]) -> int:
    old_score_vert, old_score_hor = vert_score(pattern), hor_score(pattern)
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            pattern[i] = swap_smudge(pattern[i], j)
            new_score = score(pattern, old_score_vert, old_score_hor)
            if new_score != 0:
                return new_score
            pattern[i] = swap_smudge(pattern[i], j) # swap smudge back
    return 0


def part_one(data: str) -> int:
    patterns = [[line for line in pattern.splitlines()] for pattern in data.split('\n\n')]
    return sum(score(pattern) for pattern in patterns)


def part_two(data: str) -> int:
    patterns = [[line for line in pattern.splitlines()] for pattern in data.split('\n\n')]
    return sum(fix_smudge_and_score(pattern) for pattern in patterns)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 13)
    print(part_one(input_data))
    print(part_two(input_data))
