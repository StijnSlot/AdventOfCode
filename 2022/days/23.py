from util import aoc


def new_pos(elves: set[tuple[int, int]], x: int, y: int, k: int) -> tuple[int, int]:
    ddir = [([(0, -1), (1, -1), (-1, -1)], 0, -1),   # north
            ([(0, 1), (1, 1), (-1, 1)], 0, 1),      # south
            ([(-1, 0), (-1, -1), (-1, 1)], -1, 0),   # west
            ([(1, 0), (1, -1), (1, 1)], 1, 0)]     # east
    if all((x + dx, y + dy) not in elves for dirs, _, _ in ddir for dx, dy in dirs):
        return x, y
    for i in range(4):
        to_check = (i + k) % 4
        if all((x + dx, y + dy) not in elves for dx, dy in ddir[to_check][0]):
            return x + ddir[to_check][1], y + ddir[to_check][2]
    return x, y


def simulate(elves: set[tuple[int, int]], max_steps: int = 999999) -> tuple[set[tuple[int, int]], int]:
    for k in range(max_steps):
        # for i in range(-5, 10):
        #     for j in range(-5, 10):
        #         print('#' if (j, i) in elves else '.', end='')
        #     print()
        changed = False
        new_elves = {}
        for x, y in elves:
            newx, newy = new_pos(elves, x, y, k)
            if (newx, newy) not in new_elves:
                new_elves[(newx, newy)] = []
            new_elves[(newx, newy)].append((x, y))
        elves = set()
        for newx, newy in new_elves:
            if len(new_elves[(newx, newy)]) == 1:
                if (newx, newy) != new_elves[(newx, newy)][0]:
                    changed = True
                elves.add((newx, newy))
            else:
                for x, y in new_elves[(newx, newy)]:
                    elves.add((x, y))
        if not changed:
            break
    return elves, k + 1


def parse_elves(data: str) -> set[tuple[int, int]]:
    elves = set()
    for i, line in enumerate(data.splitlines()):
        for j, x in enumerate(line):
            if x == '#':
                elves.add((j, i))
    return elves


def part_one(data: str) -> int:
    elves = parse_elves(data)
    elves, _ = simulate(elves, 10)
    minx, miny, maxx, maxy = 999999, 999999, -999999, -999999
    for x, y in elves:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    return (maxx - minx + 1) * (maxy - miny + 1) - len(elves)


def part_two(data: str) -> int:
    elves = parse_elves(data)
    _, k = simulate(elves)
    return k


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 23)
    print(part_one(input_data))
    print(part_two(input_data))
