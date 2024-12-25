from util import aoc


def read_data(data: str) -> ([tuple[int]], [tuple[int]]):
    parts = data.split('\n\n')
    locks, keys = [], []
    for part in parts:
        lines = part.splitlines()
        t = tuple(sum(1 for j in range(len(lines)) if lines[j][i] == '#') - 1 for i in range(len(lines[0])))
        if lines[0][0] == '#':
            locks.append(t)
        else:
            keys.append(t)
    return locks, keys


def part_one(data: str) -> int:
    locks, keys = read_data(data)
    print(locks)
    print(keys)
    return sum(1 for key in keys for lock in locks if all(key[i] + lock[i] < 6 for i in range(len(key))))


def part_two(data: str) -> int:
    return None


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 25)
    print(part_one(input_data))
    print(part_two(input_data))
