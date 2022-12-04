from util import aoc


def part_one(data: str) -> int:
    elfs = data.split('\n\n')
    return max(sum(int(x) for x in elf.splitlines()) for elf in elfs)


def part_two(data: str) -> int:
    elfs = data.split('\n\n')
    elfs = [sum(int(x) for x in elf.splitlines()) for elf in elfs]
    elfs = sorted(elfs)
    return sum(elfs[-3:])


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 1)
    print(part_one(input_data))
    print(part_two(input_data))
