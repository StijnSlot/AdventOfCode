from util import aoc
from math import prod


def hex_to_binary_str(hex_str: str) -> str:
    return "".join("{0:04b}".format(int(x, 16)) for x in hex_str.strip())


def read(binary: str, i: int, length: int) -> (int, int):
    return int(binary[i:i+length], 2), i + length


def operand(type_id: int, nums: list[int]) -> int:
    if type_id == 0:
        return sum(nums)
    if type_id == 1:
        return prod(nums)
    if type_id == 2:
        return min(nums)
    if type_id == 3:
        return max(nums)
    if type_id == 5:
        return 1 if nums[0] > nums[1] else 0
    if type_id == 6:
        return 1 if nums[0] < nums[1] else 0
    if type_id == 7:
        return 1 if nums[0] == nums[1] else 0


def parse(binary: str, i: int) -> (int, int, int):
    version_sum, i = read(binary, i, 3)
    type_id, i = read(binary, i, 3)
    if type_id == 4:
        value, i = read(binary, i+1, 4)
        while binary[i-5] == '1':
            x, i = read(binary, i+1, 4)
            value = 2**4 * value + x
    else:
        length_type, i = read(binary, i, 1)
        nums = []
        if length_type == 0:
            total_length, i = read(binary, i, 15)
            stop_i = i + total_length
            while i < stop_i:
                val, x, i = parse(binary, i)
                nums.append(val)
                version_sum += x
        else:
            packets, i = read(binary, i, 11)
            for _ in range(packets):
                val, x, i = parse(binary, i)
                nums.append(val)
                version_sum += x
        value = operand(type_id, nums)
    return value, version_sum, i


def part_one(data: str) -> int:
    return parse(hex_to_binary_str(data), 0)[1]


def part_two(data: str) -> int:
    return parse(hex_to_binary_str(data), 0)[0]


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 16)
    print(part_one(input_data))
    print(part_two(input_data))
