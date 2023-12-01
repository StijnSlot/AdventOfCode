from util import aoc


DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def sum_first_and_last_digit(line: str) -> int:
    digits = ''.join(filter(str.isdigit, line))
    return int(digits[0] + digits[-1])


def replace_word_digits(line: str) -> str:
    for i, digit in enumerate(DIGITS):
        line = line.replace(digit, digit + str(i + 1) + digit)
    return line


def part_one(data: str) -> int:
    return sum(sum_first_and_last_digit(line) for line in data.splitlines())


def part_two(data: str) -> int:
    return sum(sum_first_and_last_digit(replace_word_digits(line)) for line in data.splitlines())


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 1)
    print(part_one(input_data))
    print(part_two(input_data))
