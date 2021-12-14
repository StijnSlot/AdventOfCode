from util import aoc


def simulate(data: str, use_aim: bool) -> int:
    x, y, aim = 0, 0, 0
    for line in data.splitlines():
        ins, num = line.split()
        if ins == 'forward':
            x += int(num)
            if use_aim:
                y += aim * int(num)
        elif ins == 'up':
            if not use_aim:
                y += int(num)
            aim -= int(num)
        elif ins == 'down':
            if not use_aim:
                y -= int(num)
            aim += int(num)
    return x * y


def part_one(data: str) -> int:
    return simulate(data, False)


def part_two(data: str) -> int:
    return simulate(data, True)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 2)
    print(part_one(input_data))
    print(part_two(input_data))
