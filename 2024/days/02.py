from util import aoc


def is_safe(r: list[int]) -> bool:
    return all(1 <= abs(x - y) <= 3 for x, y in zip(r[::1], r[1::1])) and (
            all(y < x for x, y in zip(r[::1], r[1::1])) or
            all(x < y for x, y in zip(r[::1], r[1::1]))
        )


def is_safe_with_tolerance(r: list[int]) -> bool:
    return any(is_safe(r[:i] + r[i+1:]) for i in range(len(r)))


def part_one(data: str) -> int:
    rows = [[int(x) for x in line.split()] for line in data.splitlines()]
    return sum(1 for r in rows if is_safe(r))


def part_two(data: str) -> int:
    rows = [[int(x) for x in line.split()] for line in data.splitlines()]
    return sum(1 for r in rows if is_safe(r) or is_safe_with_tolerance(r))


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 2)
    print(part_one(input_data))
    print(part_two(input_data))
