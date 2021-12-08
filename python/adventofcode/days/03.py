from adventofcode.util import aoc


def most_common_bit(nums: list[str], i: int) -> int:
    return sum(int(nums[j][i]) for j in range(len(nums))) // (len(nums) // 2)


def part_one(data: str) -> int:
    nums = data.splitlines()
    gamma = ""
    epsilon = ""
    for i in range(len(nums[0])):
        x = most_common_bit(nums, i)
        gamma += str(x)
        epsilon += str(1 - x)
    return int(gamma, 2) * int(epsilon, 2)


def part_two(data: str) -> int:
    oxygen = data.splitlines()
    co2 = data.splitlines()
    i = 0
    while len(oxygen) > 1:
        most_common = str(most_common_bit(oxygen, i))
        oxygen = [x for x in oxygen if x[i] == most_common]
        i += 1
    i = 0
    while len(co2) > 1:
        least_common = str(1 - most_common_bit(co2, i))
        co2 = [x for x in co2 if x[i] == least_common]
        i += 1
    return int(oxygen[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    input_data = aoc.get_input(3)
    print(part_one(input_data))
    print(part_two(input_data))
