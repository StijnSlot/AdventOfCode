from util import aoc


def letter_score(x: str) -> int:
    if 'a' <= x <= 'z':
        return ord(x) - ord('a') + 1
    else:
        return ord(x) - ord('A') + 27


def part_one(data: str) -> int:
    score = 0
    for line in data.splitlines():
        halfway = len(line) // 2
        part1, part2 = line[:halfway], line[halfway:]
        x = min(set(part1) & set(part2))    # minimum just to retrieve item from set
        score += letter_score(x)
    return score


def part_two(data: str) -> int:
    lines = data.splitlines()
    score = 0
    group_size = 3
    for i in range(0, len(lines), group_size):
        group = lines[i:i+group_size]
        x = min(set(group[0]) & set(group[1]) & set(group[2]))
        score += letter_score(x)
    return score


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 3)
    print(part_one(input_data))
    print(part_two(input_data))
