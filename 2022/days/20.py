from util import aoc


def mixin(nums: list[tuple[int, int]]) -> list[tuple[int, int]]:
    N = len(nums)
    for i in range(N):
        val, j = nums[i]
        new_j = (j + val - 1) % (N - 1) + 1
        nums = [(n, k - (j < k <= new_j) + (new_j <= k < j)) for n, k in nums]
        nums[i] = (val, new_j)
    return nums


def solution(nums: list[tuple[int, int]]) -> int:
    k = next(x[1] for x in nums if x[0] == 0)
    return sum(next(x[0] for x in nums if x[1] == (k + i * 1000) % len(nums))
               for i in range(1, 4))


def part_one(data: str) -> int:
    nums = [(int(x), i) for i, x in enumerate(data.splitlines())]
    nums = mixin(nums)
    return solution(nums)


def part_two(data: str) -> int:
    nums = [(int(x) * 811589153, i) for i, x in enumerate(data.splitlines())]
    for _ in range(10):
        nums = mixin(nums)
    return solution(nums)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 20)
    print(part_one(input_data))
    print(part_two(input_data))
