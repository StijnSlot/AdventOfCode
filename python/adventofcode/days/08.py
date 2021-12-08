from adventofcode.util import aoc


def sort_str(x: str) -> str:
    return "".join(sorted(x))


def read_line(line: str) -> (list[str], list[str]):
    patterns, output = line.split(" | ")
    patterns = [sort_str(x) for x in patterns.split()]
    output = [sort_str(x) for x in output.split()]
    return patterns, output


def find_mapping(patterns: list[str]) -> dict:
    s1 = next(x for x in patterns if len(x) == 2)
    s4 = next(x for x in patterns if len(x) == 4)
    s7 = next(x for x in patterns if len(x) == 3)
    s8 = next(x for x in patterns if len(x) == 7)
    s9 = next(x for x in patterns if len(x) == 6 and all(c in x for c in s4))
    s0 = next(x for x in patterns if len(x) == 6 and x != s9 and all(c in x for c in s1))
    s6 = next(x for x in patterns if len(x) == 6 and x != s9 and x != s0)
    s3 = next(x for x in patterns if len(x) == 5 and all(c in x for c in s1))
    s5 = next(x for x in patterns if len(x) == 5 and all(c in s6 for c in x))
    s2 = next(x for x in patterns if len(x) == 5 and x != s3 and x != s5)
    return {s0: '0', s1: '1', s2: '2', s3: '3', s4: '4', s5: '5', s6: '6', s7: '7', s8: '8', s9: '9'}


def solve(line: str) -> int:
    patterns, output = read_line(line)
    digit_map = find_mapping(patterns)
    return int(''.join(digit_map[x] for x in output))


def part_one(data: str) -> int:
    return sum(1 for line in data.splitlines() for x in read_line(line)[1] if len(x) in {2, 3, 4, 7})


def part_two(data: str) -> int:
    return sum(solve(line) for line in data.splitlines())


if __name__ == "__main__":
    input_data = aoc.get_input(8)
    print(part_one(input_data))
    print(part_two(input_data))
