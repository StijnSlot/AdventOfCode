from util import aoc


def read_equations(data: str) -> (int, [int]):
    equations = []
    for line in data.splitlines():
        part1, part2 = line.split(': ')
        equations.append((int(part1), [int(x) for x in part2.split()]))
    return equations


def can_equation_be_true(i: int, left: int, nums: [int], goal: int, with_concat: bool) -> bool:
    if i == len(nums):
        return left == goal
    if left > goal:
        return False  # can never become smaller
    return can_equation_be_true(i + 1, left + nums[i], nums, goal, with_concat) \
           or can_equation_be_true(i + 1, left * nums[i], nums, goal, with_concat) \
           or (with_concat and can_equation_be_true(i + 1, int(str(left) + str(nums[i])), nums, goal, with_concat))


def part_one(data: str) -> int:
    equations = read_equations(data)
    return sum(goal for goal, nums in equations if can_equation_be_true(1, nums[0], nums, goal, False))


def part_two(data: str) -> int:
    equations = read_equations(data)
    return sum(goal for goal, nums in equations if can_equation_be_true(1, nums[0], nums, goal, True))


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 7)
    print(part_one(input_data))
    print(part_two(input_data))
