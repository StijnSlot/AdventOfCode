from util import aoc


def simulate(data: str, allow_loops: bool) -> (int, int):
    x, y, i = 0, 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = {(x, y)}
    coords = data.split(', ')
    for c in coords:
        a, b = c[0], c[1:]
        if a == 'R':
            i = (i + 1) % len(dx)
        else:
            i = (i - 1) % len(dx)
        for k in range(int(b)):
            x += dx[i]
            y += dy[i]
            if not allow_loops and (x, y) in visited:
                return x, y
            visited.add((x, y))
    return x, y


def part_one(data: str) -> int:
    x, y = simulate(data, True)
    return abs(x) + abs(y)


def part_two(data: str) -> int:
    x, y = simulate(data, False)
    return abs(x) + abs(y)


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 1)
    print(part_one(input_data))
    print(part_two(input_data))
