from util import aoc


_dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
_rect_size = 50

# Rect numbering
# 0 1 2
# 3 4 5
# 6 7 8
# 9 10 11
_rect_edge_map = {
    # square : [(new_rect, new_di, need_inverse) for each di]
    1: [None, None, (6, 0, True), (9, 0, False)],
    2: [(7, 2, True), (4, 2, False), None, (9, 3, False)],
    4: [(2, 3, False), None, (6, 1, False), None],
    6: [None, None, (1, 0, True), (4, 0, False)],
    7: [(2, 2, True), (9, 2, False), None, None],
    9: [(7, 3, False), (2, 1, False), (1, 1, False), None],
}


def do_step(grid: list[list[str]], x: int, y: int, di: int, is_rect: bool) -> tuple[bool, int, int, int]:
    dx, dy = _dd[di]
    next_x, next_y = x + dx, y + dy
    new_di = di
    if grid[next_y][next_x] == ' ':
        if is_rect:
            start_rect = 3 * ((y - 1) // _rect_size) + ((x - 1) // _rect_size)
            new_rect, new_di, inverse = _rect_edge_map[start_rect][di]
            new_dx, new_dy = _dd[new_di]
            new_rect_x, new_rect_y = _rect_size * (new_rect % 3) + 1, _rect_size * (new_rect // 3) + 1  # top left
            edge_pos = abs(dy) * ((x - 1) % _rect_size) + abs(dx) * ((y - 1) % _rect_size)    # amount of steps from top/left
            next_x = new_rect_x + (
                (_rect_size - edge_pos - 1 if inverse else edge_pos)
                if new_dy != 0
                else (_rect_size - 1 if new_dx == -1 else 0))
            next_y = new_rect_y + (
                (_rect_size - edge_pos - 1 if inverse else edge_pos)
                if new_dx != 0
                else (_rect_size - 1 if new_dy == -1 else 0))
        else:
            next_x -= dx
            next_y -= dy
            while grid[next_y][next_x] != ' ':
                next_x -= dx
                next_y -= dy
            next_x += dx
            next_y += dy
    if grid[next_y][next_x] == '#':
        return False, x, y, di
    return True, next_x, next_y, new_di


def simulate(grid: list[list[str]], path: str, is_rect: True) -> int:
    x, y = next(i for i, a in enumerate(grid[1]) if a == '.'), 1
    di = 0
    k = 0
    while k < len(path):
        turn_k = next((i + k for i, a in enumerate(path[k:]) if a in ['L', 'R']), len(path))
        steps = int(path[k:turn_k])
        for i in range(steps):
            can_step, x, y, di = do_step(grid, x, y, di, is_rect)
            if not can_step:
                break
        if turn_k != len(path):
            if path[turn_k] == 'R':
                di = (di + 1) % len(_dd)
            else:
                di = (di - 1) % len(_dd)
        k = turn_k + 1
    return 1000 * y + 4 * x + di


def parse_input(data: str) -> tuple[str, list[list[str]]]:
    grid = []
    grid_lines, path = data.split('\n\n')
    for line in grid_lines.splitlines():
        grid.append([c for c in line])
    max_x = max(len(line) for line in grid)
    for i in range(len(grid)):
        grid[i] = [' '] + grid[i] + [' ' for _ in range(len(grid[i]), max_x + 2)]
    return path, [[' ' for _ in range(max_x + 3)]] + grid + [[' ' for _ in range(max_x + 3)]]


def part_one(data: str) -> int:
    path, grid = parse_input(data)
    return simulate(grid, path, False)


def part_two(data: str) -> int:
    path, grid = parse_input(data)
    return simulate(grid, path, True)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 22)
    print(part_one(input_data))
    print(part_two(input_data))
