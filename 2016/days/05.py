from util import aoc
from functools import lru_cache
import hashlib


@lru_cache(maxsize=9999999)
def md5_hash(prefix: str, x: int) -> str:
    return hashlib.md5((prefix + str(x)).encode()).hexdigest()[:7]


def find_next_md5(prefix: str, start: int):
    i = start
    while md5_hash(prefix, i)[:5] != "00000":
        i += 1
    return md5_hash(prefix, i), i + 1


def part_one(data: str) -> str:
    result, j = "", 0
    for i in range(8):
        md5, j = find_next_md5(data, j)
        result += md5[5]
    return result


def part_two(data: str) -> str:
    result, j = [None for _ in range(8)], 0
    while None in result:
        md5, j = find_next_md5(data, j)
        pos, c = md5[5], md5[6]
        if '0' <= pos <= '7' and result[int(pos)] is None:
            result[int(pos)] = c
    return "".join(result)


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 5)
    print(part_one(input_data))
    print(part_two(input_data))
