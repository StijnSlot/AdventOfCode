from util import aoc


_dirs = {'R': (0, 1), 'U': (1, 0), 'L': (0, -1), 'D': (-1, 0)}


def update(rope: list[tuple[int, int]], dx: int, dy: int) -> list[tuple[int, int]]:
    new_rope = [(rope[0][0] + dx, rope[0][1] + dy)]
    for i in range(1, len(rope)):
        tx, ty = new_rope[i-1][0] - rope[i][0], new_rope[i-1][1] - rope[i][1]
        if abs(tx) > 1 or abs(ty) > 1:
            norm_tx = 0 if tx == 0 else tx // abs(tx)
            norm_ty = 0 if ty == 0 else ty // abs(ty)
            new_rope.append((rope[i][0] + norm_tx, rope[i][1] + norm_ty))
        else:
            new_rope.append(rope[i])
    return new_rope


def simulate(data: str, rope: list[tuple[int, int]]) -> set[tuple[int, int]]:
    visited = set()
    for line in data.splitlines():
        a, b = line.split()
        dx, dy = _dirs[a]
        for i in range(int(b)):
            rope = update(rope, dx, dy)
            visited.add(rope[-1])
    return visited


def part_one(data: str) -> int:
    rope = [(0, 0), (0, 0)]
    visited = simulate(data, rope)
    return len(visited)


def part_two(data: str) -> int:
    rope = [(0, 0) for _ in range(10)]
    visited = simulate(data, rope)
    return len(visited)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 9)
    print(part_one(input_data))
    print(part_two(input_data))
