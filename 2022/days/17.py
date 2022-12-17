from util import aoc


hor_line_piece = [(0, 0), (1, 0), (2, 0), (3, 0)]
plus_piece = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]
corner_piece = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
ver_line_piece = [(0, 0), (0, 1), (0, 2), (0, 3)]
square_piece = [(0, 0), (1, 0), (0, 1), (1, 1)]
piece_order = [hor_line_piece, plus_piece, corner_piece, ver_line_piece, square_piece]


def relative_height(max_y: list[int]):
    return tuple(y - max(max_y) for y in max_y)


def simulate_falling_rock(grid: list[list[str]], piece: list[tuple[int, int]], wind_x: int) -> tuple[bool, list[tuple[int, int]]]:
    # wind movement
    new_piece = [(x + wind_x, y) for x, y in piece]
    if all(grid[y][x] == '.' for x, y in new_piece):
        piece = new_piece

    # down movement
    new_piece = [(x, y - 1) for x, y in piece]
    if any(grid[y][x] != '.' for x, y in new_piece):
        return True, piece

    return False, new_piece


def simulate(data: str, nr_of_rocks: int, do_memo: int = False) -> int:
    grid = [list('+-------+')] + [list('|.......|') for _ in range(min(4 * nr_of_rocks, 1000000))]
    i, j = 0, 0
    max_y = [0 for _ in range(1, 8)]    # store max height for each column
    memo = {}
    for k in range(nr_of_rocks):
        if do_memo:
            # for part 2
            rel_pos = relative_height(max_y)
            rel_i, rel_j = i % len(piece_order), j % len(data)
            if (rel_i, rel_j, rel_pos) in memo:
                last_i, last_height = memo[(rel_i, rel_j, rel_pos)]
                if (nr_of_rocks - i) % (i - last_i) == 0:   # easier to do calculation
                    cur_height = max(max_y)
                    iter_left = (nr_of_rocks - i) // (i - last_i)
                    return cur_height + (cur_height - last_height) * iter_left
            memo[(rel_i, rel_j, relative_height(max_y))] = i, max(max_y)

        piece = piece_order[i % len(piece_order)]
        piece = [(x + 3, y + max(max_y) + 4) for x, y in piece]  # starting spot
        while True:
            wind_x = 1 if data[j % len(data)] == '>' else -1
            j += 1
            stopped, piece = simulate_falling_rock(grid, piece, wind_x)
            if stopped:
                # update grid with stopped rock
                for x, y in piece:
                    grid[y][x] = '#'
                max_y = [max(max_y[l-1], max((y for x, y in piece if x == l), default=0)) for l in range(1, 8)]
                break
        i += 1
    return max(max_y)


def part_one(data: str) -> int:
    return simulate(data, 2022)


def part_two(data: str) -> int:
    return simulate(data, 1000000000000, True)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 17)
    print(part_one(input_data))
    print(part_two(input_data))
