from util import aoc
from statistics import median, mean


def sum_steps(n: int) -> int:
    return n * (n + 1) // 2


def part_one(data: str) -> int:
    nums = [int(x) for x in data.split(',')]
    med = median(nums)
    return sum(abs(med - x) for x in nums)


def part_two(data: str) -> int:
    nums = [int(x) for x in data.split(',')]
    avg = mean(nums)
    return sum(sum_steps(abs(avg - x)) for x in nums)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 7)
    print(part_one(input_data))
    print(part_two(input_data))
