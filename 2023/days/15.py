from util import aoc
from functools import reduce


def hash_word(word: str) -> int:
    return reduce(lambda x, y: (17 * (x + ord(y))) % 256, word, 0)


def part_one(data: str) -> int:
    return sum(hash_word(x) for x in data.replace('\n', '').split(','))


def part_two(data: str) -> int:
    ops = [x for x in data.replace('\n', '').split(',')]
    lenses = {}
    focal_lengths = {}
    for op_str in ops:
        if '=' in op_str:
            lens, focal_length = op_str.split('=')
            hash_lens = hash_word(lens)
            if hash_lens not in lenses:
                lenses[hash_lens] = [lens]
            elif lens not in lenses[hash_lens]:
                lenses[hash_lens].append(lens)
            focal_lengths[lens] = int(focal_length)
        else:
            lens = op_str[:-1]
            hash_lens = hash_word(lens)
            if hash_lens in lenses and lens in lenses[hash_lens]:
                lenses[hash_lens].remove(lens)
    return sum((hash_word(lens) + 1) * (i + 1) * focal_lengths[lens] for x in lenses for i, lens in enumerate(lenses[x]))


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 15)
    print(part_one(input_data))
    print(part_two(input_data))
