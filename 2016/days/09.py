from util import aoc


def length(data: str, recursion: bool, start: int = 0, stop: int = -1) -> int:
    total, i = 0, start
    while i < len(data) and (stop == -1 or i < stop):
        if data[i] == '(':
            j = data[i:].index(')')
            a, b = data[i+1:i+j].split('x')
            i += j + 1
            total += (length(data, recursion, i, i + int(a)) if recursion else int(a)) * int(b)
            i += int(a)
        else:
            total += 1
            i += 1
    return total


def part_one(data: str) -> int:
    return length(data, False)


def part_two(data: str) -> int:
    return length(data, True)


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 9)
    print(part_one(input_data))
    print(part_two(input_data))
