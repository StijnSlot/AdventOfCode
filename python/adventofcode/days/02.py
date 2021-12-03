from adventofcode.util import aoc


def part_one(data):
    x, y = 0, 0
    for line in data.splitlines():
        ins, num = line.split()
        if ins == 'forward':
            x += int(num)
        elif ins == 'up':
            y += int(num)
        elif ins == 'down':
            y -= int(num)
    return x * y


def part_two(data):
    x, y, aim = 0, 0, 0
    for line in data.splitlines():
        ins, num = line.split()
        if ins == 'forward':
            x += int(num)
            y += aim * int(num)
        elif ins == 'up':
            aim -= int(num)
        elif ins == 'down':
            aim += int(num)
    return x * y


if __name__ == "__main__":
    input_data = aoc.get_input(2)
    print(part_one(input_data))
    print(part_two(input_data))
