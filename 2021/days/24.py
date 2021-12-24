from functools import cache

from util import aoc


def get_val_b(mem: dict[str, int], b: str):
    try:
        return int(b)
    except ValueError:
        return mem[b]


def instruction(mem: dict[str, int], ins: str, a: str, b: str):
    val_b = get_val_b(mem, b)
    if ins == 'inp':
        mem[a] = val_b
    elif ins == 'add':
        mem[a] += val_b
    elif ins == 'mul':
        mem[a] *= val_b
    elif ins == 'div':
        mem[a] //= val_b
    elif ins == 'mod':
        mem[a] %= val_b
    elif ins == 'eql':
        mem[a] = 1 if mem[a] == val_b else 0


def run_program(program: list[str], inp: int, z: int) -> int:
    mem = {'w': 0, 'x': 0, 'y': 0, 'z': z}
    for line in program:
        parts = line.split()
        if parts[0] == 'inp':
            ins, a, b = parts[0], parts[1], str(inp)
        else:
            ins, a, b = parts
        instruction(mem, ins, a, b)
    return mem['z']


def solve(programs: list[list[str]], highest: bool):
    @cache
    def solve_digit(i, z, highest):
        if i == 14:
            return z == 0, ''
        if abs(z) >= 100000000:
            return False, ''
        k_range = reversed(range(1, 10)) if highest else range(1, 10)
        for k in k_range:
            new_z = run_program(programs[i], k, z)
            solved, x = solve_digit(i+1, new_z, highest)
            if solved:
                return True, str(k) + x
        return False, ''
    return solve_digit(0, 0, highest)


def part_one(data: str) -> int:
    programs = [['inp w'] + part.splitlines()[1:] for part in data.split('inp w')[1:]]
    return solve(programs, True)


def part_two(data: str) -> int:
    programs = [['inp w'] + part.splitlines()[1:] for part in data.split('inp w')[1:]]
    return solve(programs, False)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 24)
    # print(part_one(input_data))
    print(part_two(input_data))
